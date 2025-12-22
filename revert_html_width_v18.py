
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-17.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert HTML Width
# Target (Patched in v17): `className:"flex flex-col items-center justify-end h-full w-[60px] mx-3 group"`
# Revert to `w-24`.
target_width = 'className:"flex flex-col items-center justify-end h-full w-[60px] mx-3 group"'
repl_width = 'className:"flex flex-col items-center justify-end h-full w-24 mx-3 group"'

count = 0
if target_width in content:
    content = content.replace(target_width, repl_width)
    count += 1
    print("HTML Width reverted to w-24.")
else:
    print("Error: HTML Width w-[60px] target not found.")
    # Fallback search
    idx = content.find('w-[60px]')
    if idx != -1:
        print(f"Found w-[60px] at {idx}")

# 2. Dump Incidence Rate Ratio (Gauge?)
# HTML
idx_irr = content.find('Incidence Rate Ratio')
if idx_irr != -1:
    print("\nFound Incidence Rate Ratio (HTML/PDF) at", idx_irr)
    print("--- Context IRR ---")
    print(content[idx_irr-500:idx_irr+500])
    
    # Search for next occurence
    idx_irr2 = content.find('Incidence Rate Ratio', idx_irr+1)
    if idx_irr2 != -1:
        print("\nFound Incidence Rate Ratio (2) at", idx_irr2)
        print("--- Context IRR 2 ---")
        print(content[idx_irr2-500:idx_irr2+500])

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Patches updated: {count}")
