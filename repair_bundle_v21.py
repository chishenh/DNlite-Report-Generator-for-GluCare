
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-20.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Target broken sequence from Dump 746
# `...needle})]})});})},Fm=`
# It has an extra `)` (and maybe `}`) from the merge.
# I want: `...needle})]})});},Fm=` (End of function `}`, Comma `,`, Next Var `Fm=`)

target_broken = 'fill:V0.needle})]})});})},Fm='
repl_fixed = 'fill:V0.needle})]})});},Fm='

if target_broken in content:
    content = content.replace(target_broken, repl_fixed)
    print("Repaired v21 syntax (removed extra chars).")
else:
    print("Error: Broken target string not found. Trying flexible search.")
    # Fallback: Just search for `});})},Fm=` and replace with `});},Fm=`
    fallback_target = '});})},Fm='
    fallback_repl = '});},Fm='
    if fallback_target in content:
        content = content.replace(fallback_target, fallback_repl)
        print("Repaired v21 syntax (Fallback match).")
    else:
        print("Error: Fallback target also not found.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
