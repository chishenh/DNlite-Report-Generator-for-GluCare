
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-14.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Target: Non-DM ESRD 1.6 height "43%"
# Context: `children:"1.6"}),me.jsx(hr,{style:{width:60,height:"43%",backgroundColor:Br.red`

target_nondm_16 = 'children:"1.6"}),me.jsx(hr,{style:{width:60,height:"43%",backgroundColor:Br.red'
repl_nondm_16 = 'children:"1.6"}),me.jsx(hr,{style:{width:60,height:"16%",backgroundColor:Br.red'

count = 0
if target_nondm_16 in content:
    content = content.replace(target_nondm_16, repl_nondm_16)
    count += 1
    print("Corrected Non-DM ESRD height from 43% to 16%.")
else:
    print("Error: Non-DM height target 43% not found.")
    idx = content.find('children:"1.6"')
    if idx != -1:
        print("Context around 1.6:")
        print(content[idx:idx+200])

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Patches updated: {count}")
