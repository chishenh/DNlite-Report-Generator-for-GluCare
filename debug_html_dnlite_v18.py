
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-17.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search html unique string for DNlite header
# Previous dump showed: `me.jsx("th",{className:"border border-slate-300 p-2 font-bold text-slate-900 bg-slate-50 text-center w-1/3",children:"DNlite (uPTM-FetA/UCr)"})`
# I'll search for `children:"DNlite (uPTM-FetA/UCr)"`
idx = content.find('children:"DNlite (uPTM-FetA/UCr)"')
if idx != -1:
    print("Found HTML DNlite Header at", idx)
    print("--- HTML DNlite Context ---")
    print(content[idx:idx+3000])
else:
    print("HTML DNlite Header not found.")
