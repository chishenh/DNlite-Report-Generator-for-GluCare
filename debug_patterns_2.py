
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-C1D2uKbX.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Diagnostic for HTML chart (Fm component usage)
search_str = 'style:{backgroundColor:"#f8fafc"},children:[me.jsx(Fm'
idx = content.find(search_str)
if idx != -1:
    print(f"Found HTML chart pattern at {idx}")
else:
    print("HTML chart pattern NOT FOUND (checking for old pattern...)")
    old_str = 'style:{backgroundColor:"#dce3eb"},children:[me.jsx(Fm'
    idx_old = content.find(old_str)
    if idx_old != -1:
        print(f"Found OLD HTML chart pattern at {idx_old} -> Needs update")
    else:
        print("Neither OLD nor NEW HTML chart pattern found.")
