#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""复算本库的 wikilink 解析情况与 .base 视图命中情况。

为什么要它：校验记录里的每个数字都应该能被独立复算，而不是靠口述。
上一轮评估者就点出过「过滤求值脚本未留在库里」，只能自己重写一遍——这份就是它。

做三件事：
1. wikilink：扫描全部 .md（跳过 .obsidian/ .claudian/ clear/），
   并分别给出「字面扫描」与「实际渲染口径」两个数——
   代码块与行内代码里的 [[…]] 在 Obsidian 里不会渲染成链接，不该混进悬空统计。
2. .base：按 Obsidian 自身 inFolder / tagMatches 的实现求值每个视图，列出命中文件。
   两种施受方向都算一遍（见 tag_matches 的说明）；本库的过滤式用的都是整条叶子标签，
   两个方向结果相同，所以结论不受方向影响。
3. 输出 JSON 到 clear/models/base_filter_check.out.json，供报告引用。

用法：python3 clear/models/base_filter_check.py
"""
import datetime
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKIP = {'.obsidian', '.claudian', 'clear', '.git', '.trash', '.stfolder'}
OUT = Path(__file__).resolve().parent / 'base_filter_check.out.json'
# 报告 §一 交付物清单里逐个报大小/行数的文件
ARTIFACTS = ['home.md', 'AGENTS.md', '知识库工作流.md', '收集箱/收集箱.md', '项目/项目.md',
             '数据库/收集箱数据库.base', '数据库/项目数据库.base', '模板/项目模板.md',
             'clear/models/base_filter_check.py', 'clear/reports/知识库重构-校验记录.md']


def rel(p):
    return str(Path(p).relative_to(ROOT)).replace('\\', '/')


def walk():
    out = []
    for p in ROOT.rglob('*'):
        if not p.is_file():
            continue
        if any(part in SKIP for part in p.relative_to(ROOT).parts):
            continue
        out.append(p)
    return sorted(out)


FILES = walk()
MD = [p for p in FILES if p.suffix == '.md']

# ---------- 名称索引（贴近 Obsidian 的 wikilink 解析：全路径优先，其次文件名） ----------
by_rel, by_name = {}, {}
for p in FILES:
    by_rel.setdefault(rel(p), []).append(p)
    by_name.setdefault(p.name, []).append(p)
    if p.suffix == '.md':
        by_rel.setdefault(str(Path(rel(p)).with_suffix('')), []).append(p)
        by_name.setdefault(p.stem, []).append(p)


def resolve(target):
    t = target.strip().strip('/')
    if not t:
        return None
    for idx in (by_rel, by_name):
        hit = idx.get(t)
        if hit and len(hit) == 1:
            return hit[0]
    hit = by_name.get(t + '.md')
    if hit and len(hit) == 1:
        return hit[0]
    return None


LINK = re.compile(r'!?\[\[([^\[\]\n]+)\]\]')
INLINE_CODE = re.compile(r'`[^`\n]*`')


def strip_target(raw):
    return raw.split('|')[0].split('#')[0].strip()


# ---------- 1. wikilink 扫描 ----------
rows = []
for p in MD:
    in_fence = False
    lines = p.read_text(encoding='utf-8', errors='replace').split('\n')
    # frontmatter 边界：第 1 行是 --- 时到下一个 --- 为止（只用来区分「正文里写坏的链接」）
    fm_end = 0
    if lines and lines[0].strip() == '---':
        for _i in range(1, len(lines)):
            if lines[_i].strip() == '---':
                fm_end = _i + 1
                break
    for n, line in enumerate(lines, 1):
        if line.lstrip().startswith('```'):
            in_fence = not in_fence
            continue
        spans = [(m.start(), m.end()) for m in INLINE_CODE.finditer(line)]
        for m in LINK.finditer(line):
            if in_fence:
                where = 'fence'
            elif any(a <= m.start() < b for a, b in spans):
                where = 'inline_code'
            else:
                where = 'text'
            rows.append({
                'file': rel(p), 'line': n,
                'raw': m.group(0), 'target': strip_target(m.group(1)),
                'where': where, 'in_frontmatter': n <= fm_end,
                'resolved': resolve(strip_target(m.group(1))) is not None,
            })

for r in rows:
    if r['resolved']:
        r['bucket'] = 'resolved'
    elif r['where'] in ('fence', 'inline_code'):
        r['bucket'] = 'code'                      # Obsidian 不把代码里的 [[…]] 当链接
    elif r['file'].startswith('模板/'):
        r['bucket'] = 'template_placeholder'      # 模板占位符，套用前本就没有目标
    elif r['in_frontmatter'] and (r['file'].startswith('Clippings/') or r['file'].startswith('收集箱/')):
        r['bucket'] = 'input_content'             # 只认剪藏 frontmatter 的 author 等字段，属输入内容本身
        # 正文（含 AI 自己写进 收集箱/ 的笔记）里指空的链接一律算 dangling，
        # 否则「在收集箱里写坏链接」会被这个归类悄悄放过。
    else:
        r['bucket'] = 'dangling'                  # 真正的悬空链接

UNRESOLVED = [r for r in rows if not r['resolved']]
RENDERED_UNRESOLVED = [r for r in UNRESOLVED if r['bucket'] != 'code']


def tally(items, key):
    d = {}
    for r in items:
        d[r[key]] = d.get(r[key], 0) + 1
    return dict(sorted(d.items(), key=lambda kv: -kv[1]))


# ---------- 2. .base 求值 ----------
def frontmatter_tags(p):
    text = p.read_text(encoding='utf-8', errors='replace')
    if not text.startswith('---'):
        return []
    end = text.find('\n---', 3)
    if end < 0:
        return []
    block = text[3:end]
    tags = None
    try:
        import yaml
        data = yaml.safe_load(block) or {}
        tags = data.get('tags') if isinstance(data, dict) else None
    except Exception:
        for m in re.finditer(r'^\s*-\s*"?([^"\n]+?)"?\s*$', block, re.M):
            if tags is None:
                tags = []
            tags.append(m.group(1))
    if isinstance(tags, str):
        tags = [tags]
    return [str(t) for t in (tags or [])]


TAGS = {rel(p): frontmatter_tags(p) for p in MD}


def norm(tag):
    t = str(tag).strip()
    return (t[1:] if t.startswith('#') else t).lower()


def tag_matches(query, file_tag, direction):
    """两种施受方向都实现，因为 asar 里那行代码的方向容易被读反。

    direction='file_prefix' ：文件标签以查询为前缀 —— **这才是 asar 的真实方向**。
        调用点（字节 2938182）是 s.tagMatches(u)：s 取自 e.getTags()（被查文件的标签），
        u 是查询值，所以 tagMatches 里的 this 是文件标签。表现为 hasTag("status") 命中 status 与 status/进行中。
    direction='query_prefix'：查询以文件标签为前缀 —— 我一度读反过，保留只为对照 direction_agrees。
    本库的过滤式一律写整条叶子标签（status/进行中、主页、status/已归档），两者等价。
    """
    q, f = norm(query), norm(file_tag)
    if direction == 'query_prefix':
        return q == f or (q.startswith(f) and q[len(f):len(f) + 1] == '/')
    return q == f or (f.startswith(q) and f[len(q):len(q) + 1] == '/')


CALL = re.compile(r'^file\.(inFolder|hasTag)\(\s*"([^"]*)"\s*\)$')


def ev(node, path, tags, direction):
    if node is None:
        return True
    if isinstance(node, str):
        m = CALL.match(node.strip())
        if not m:
            raise ValueError('无法识别的筛选式：%r' % node)
        fn, arg = m.group(1), m.group(2)
        if fn == 'inFolder':
            return path.startswith(arg + '/')       # asar: path.startsWith(folder + "/")
        return any(tag_matches(arg, t, direction) for t in tags)
    if isinstance(node, dict):
        if len(node) != 1:
            raise ValueError('筛选组只应有一个键：%r' % node)
        k, v = list(node.items())[0]
        if k == 'and':
            return all(ev(x, path, tags, direction) for x in v)
        if k == 'or':
            return any(ev(x, path, tags, direction) for x in v)
        if k == 'not':
            # asar: 组内任一子条件为真则整体为假（labelNoneOfTheFollowing）
            return not any(ev(x, path, tags, direction) for x in v)
        raise ValueError('未知的筛选键：%r' % k)
    if isinstance(node, list):
        return all(ev(x, path, tags, direction) for x in node)
    raise ValueError('无法识别的筛选节点：%r' % node)


bases = []
for b in sorted((ROOT / '数据库').glob('*.base')):
    import yaml
    data = yaml.safe_load(b.read_text(encoding='utf-8'))
    gfilter = data.get('filters')
    views = []
    for v in (data.get('views') or []):
        vf = v.get('filters')
        hits = {}
        for d in ('query_prefix', 'file_prefix'):
            hits[d] = sorted(
                rel(p) for p in MD
                if ev(gfilter, rel(p), TAGS.get(rel(p), []), d) and ev(vf, rel(p), TAGS.get(rel(p), []), d)
            )
        views.append({'name': v.get('name'), 'type': v.get('type'),
                      'filter': vf, 'hits': hits['file_prefix'],
                      'hits_by_direction': hits,
                      'direction_agrees': hits['query_prefix'] == hits['file_prefix']})
    bases.append({'path': rel(b), 'view_count': len(views), 'views': views})

result = {
    'generated_at': datetime.datetime.now().astimezone().isoformat(timespec='seconds'),
    'scope': {
        'vault_root': '.',
        'files_scanned': len(MD),
        'skipped_dirs': sorted(SKIP),
        'note': 'clear/ 是 AI 自己的运行目录，其内的 [[…]] 示例不计入本库链接统计',
    },
    'wikilinks': {
        'total_literal': len(rows),
        'total_rendered': len([r for r in rows if r['where'] == 'text']),
        'unresolved_literal': len(UNRESOLVED),
        'unresolved_rendered': len(RENDERED_UNRESOLVED),
        'by_bucket': tally(UNRESOLVED, 'bucket'),
        'by_bucket_rendered': tally(RENDERED_UNRESOLVED, 'bucket'),
        'by_file': tally(UNRESOLVED, 'file'),
        'by_bucket_file': {
            b: tally([r for r in UNRESOLVED if r['bucket'] == b], 'file')
            for b in sorted({r['bucket'] for r in UNRESOLVED})
        },
        # 全量明细（不筛口径）：每条带 rendered 标记，谁都能按自己的口径重算
        'unresolved_detail': [
            dict({k: r[k] for k in ('file', 'line', 'raw', 'target', 'where', 'bucket')},
                 rendered=(r['bucket'] != 'code'))
            for r in UNRESOLVED
        ],
    },
    'bases': bases,
    # 报告 §一 的「大小/行数」从这里取，重跑即刷新，避免手抄后漂移
    'artifacts': {
        a: {'bytes': (ROOT / a).stat().st_size,
            'lines': len((ROOT / a).read_text(encoding='utf-8').split('\n'))}
        for a in ARTIFACTS if (ROOT / a).exists()
    },
}
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# ---------- 3. 人读摘要 ----------
w = result['wikilinks']
print('扫描 .md 文件：%d 个（跳过 %s）' % (len(MD), '/'.join(sorted(SKIP))))
print('wikilink 字面扫描 %d 条；实际渲染口径 %d 条' % (w['total_literal'], w['total_rendered']))
print('未解析（字面）%d 条 → %s' % (w['unresolved_literal'], w['by_bucket']))
print('未解析（渲染口径）%d 条 → %s' % (w['unresolved_rendered'], w['by_bucket_rendered']))
for b in ('code', 'template_placeholder', 'input_content', 'dangling'):
    items = [r for r in UNRESOLVED if r['bucket'] == b]
    if not items:
        continue
    print('   [%s] %d 条（是否计入渲染口径：%s）' % (b, len(items), '否' if b == 'code' else '是'))
    for r in items:
        print('      · %s:%d %s  [%s]' % (r['file'], r['line'], r['raw'], r['where']))
print()
for b in bases:
    print('%s（%d 个视图）' % (b['path'], b['view_count']))
    for v in b['views']:
        flag = '' if v['direction_agrees'] else '  ⚠ 两种方向结果不同'
        print('   - %s：命中 %d 个 %s%s' % (v['name'], len(v['hits']), v['hits'], flag))
print()
print('已写出 %s' % rel(OUT))
