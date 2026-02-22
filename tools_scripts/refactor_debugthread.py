from pathlib import Path
import re

root = Path('coop_mod')
files = sorted(root.glob('*.scr'))
pat = re.compile(r'^(\s*)if\((level\.cMTE_coop_[^)]+)\)\{.*?println\(\s*"-#-#- thread\s+([^"]+)".*$')

changed_files = []
replaced_total = 0

for p in files:
    text = p.read_text(encoding='utf-8', errors='ignore')
    lines = text.splitlines()
    out = []
    changed = False
    gate_var = None
    replacements_in_file = 0

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('//'):
            out.append(line)
            continue

        m = pat.match(line)
        if m:
            indent, gate, label = m.groups()
            gate_var = gate_var or gate
            out.append(f'{indent}thread debugThread "{label}"')
            changed = True
            replacements_in_file += 1
            continue

        out.append(line)

    if not changed:
        continue

    if 'debugThread local.label:{' not in '\n'.join(out):
        helper = [
            '',
            '//[204] cleanup - central debug print helper to reduce repeated preamble code',
            '//==========================================================================',
            'debugThread local.label:{',
            '//==========================================================================',
            f'\tif({gate_var}){{',
            '\t\tif(!level.cMTE){ level.cMTE = 0 }',
            '\t\tlevel.cMTE++',
            '\t\tprintln( "-#-#- thread " + local.label + "->" + level.cMTE )',
            '\t}',
            '}end',
            ''
        ]
        out.extend(helper)

    p.write_text('\n'.join(out) + '\n', encoding='utf-8')
    changed_files.append((p.as_posix(), replacements_in_file))
    replaced_total += replacements_in_file

print(f'CHANGED_FILES {len(changed_files)}')
print(f'REPLACED_TOTAL {replaced_total}')
for fp, cnt in changed_files:
    print(f'{cnt:4} {fp}')
