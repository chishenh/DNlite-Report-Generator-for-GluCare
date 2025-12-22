
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-17.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Dump b3e
idx_b3e = content.find('b3e=')
if idx_b3e != -1:
    print("Found b3e at", idx_b3e)
    print(content[idx_b3e:idx_b3e+1500])
else:
    print("b3e definition not found via 'b3e='.")
    # Search usage to confirm name
    idx_usage = content.find('jsx(b3e,')
    if idx_usage != -1:
        print("Found usage of b3e at", idx_usage)
        
# 2. Dump Fm Usages
print("\n--- Fm Usages ---")
start = 0
found_60 = False
while True:
    idx = content.find('jsx(Fm', start)
    if idx == -1:
        break
    # Check width in the vicinity
    ctx = content[idx:idx+300]
    print(f"Match at {idx}: {ctx}")
    if 'w-[60px]' in ctx:
        found_60 = True
    start = idx + 1

if found_60:
    print("\nConfirmed presence of w-[60px].")
else:
    print("\nNo w-[60px] found. Bars seem to be w-24?")
