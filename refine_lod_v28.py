
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-27.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Target: LOD strings
# ye<5.428?(U._disp_uptm="<5.428",U._disp_dnlite="<7.53",be=0)
# ye>250?(U._disp_uptm=">250",U._disp_dnlite=">7.53",be=999)

replacements = [
    ('U._disp_uptm="<5.428"', 'U._disp_uptm="<5.43"'),
    ('U._disp_uptm=">250"', 'U._disp_uptm=">250.00"')
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"Replaced {old} with {new}")
    else:
        print(f"Could not find {old}")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
