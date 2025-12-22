
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-13.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Target: ESRD Low Bar logic in PDF
# Context from previous dump (2235236):
# `children:"1"}),me.jsx(hr,{style:{width:60,height:"28%",backgroundColor:Br.teal`

target_esrd_low = 'children:"1"}),me.jsx(hr,{style:{width:60,height:"28%",backgroundColor:Br.teal'
repl_esrd_low = 'children:"1"}),me.jsx(hr,{style:{width:60,height:"10%",backgroundColor:Br.teal'

count = 0
if target_esrd_low in content:
    content = content.replace(target_esrd_low, repl_esrd_low)
    count += 1
    print("Updated ESRD Low Bar height from 28% to 10%.")
else:
    print("Error: ESRD Low Bar target not found.")
    # Fallback search if context slightly different
    idx = content.find('height:"28%"')
    if idx != -1:
        print("Found 'height:\"28%\"' at other location:")
        print(content[idx-50:idx+50])

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Patches updated: {count}")
