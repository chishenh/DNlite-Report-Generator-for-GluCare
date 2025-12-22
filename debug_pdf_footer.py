
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-7.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate Uk component start again
idx_uk = content.find('Uk=({data:e,logo:t,companyLogo:r,inspector:n})')
if idx_uk != -1:
    # Look for "Lab. Director" after this point
    idx_lab = content.find("Lab. Director", idx_uk)
    if idx_lab != -1:
        print(f"Found 'Lab. Director' in PDF logic at {idx_lab}")
        s = max(0, idx_lab - 500)
        e = min(len(content), idx_lab + 500)
        print(content[s:e])
    else:
        print("Could not find 'Lab. Director' in PDF logic")
else:
    print("Could not find Uk component")
