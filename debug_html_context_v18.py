
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-17.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Search for HTML Remark (which I centered in V16!)
# So search for `text-center` version.
remark_target = 'className:"border border-slate-300 p-2 text-center w-1/3",children:"Remark"'
idx_rem = content.find(remark_target)
if idx_rem != -1:
    print(f"Found HTML Remark at {idx_rem}")
    print("--- HTML Table Context (Following) ---")
    print(content[idx_rem:idx_rem+3000])
else:
    print("HTML Remark target not found.")
    # Debug: Search "Remark" again to see current state
    idx = content.find('children:"Remark"')
    if idx != -1:
        print(f"Found generic Remark at {idx}: {content[idx-50:idx+100]}")

# 2. Search for w-[60px]
idx_w = content.find('w-[60px]')
if idx_w != -1:
    print(f"\nFound w-[60px] at {idx_w}")
    print(content[idx_w-100:idx_w+100])
else:
    print("\nw-[60px] not found.")
