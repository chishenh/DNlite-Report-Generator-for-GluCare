
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-15.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# PDF Table: Search for "Remark"
idx_remark = content.find('children:"Remark"')
if idx_remark != -1:
    print("Found 'Remark' at", idx_remark)
    print("--- Context Table (Remark) ---")
    print(content[idx_remark-200:idx_remark+1500])
else:
    print("Error: 'Remark' not found.")

# HTML Component: Fm
# Search for `function Fm` or `const Fm`.
# Or usage: `me.jsx(Fm` to find variable name if minified differently.
# Assuming `Fm` is the name from previous dump.
idx_fm = content.find('const Fm=') # Try const
if idx_fm == -1:
    idx_fm = content.find('function Fm') # Try function
if idx_fm == -1:
    idx_fm = content.find('var Fm=') # Try var
if idx_fm != -1:
    print("\nFound Fm definition at", idx_fm)
    print("--- Context Fm ---")
    print(content[idx_fm:idx_fm+500])
else:
    print("Fm definition not found (might be imported or renamed in dump vs reality).")
    # Actually, previous dump explicitly showed `me.jsx(Fm,...)`. So `Fm` IS the name in scope.
    # It might be `Fm=({value...` (arrow func assignment).
    idx_fm_arrow = content.find('Fm=')
    if idx_fm_arrow != -1:
        print("\nFound Fm= at", idx_fm_arrow)
        print("--- Context Fm= ---")
        print(content[idx_fm_arrow:idx_fm_arrow+500])
