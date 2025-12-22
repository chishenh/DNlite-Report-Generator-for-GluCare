
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-7.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Target string from dump
# me.jsxs(hr,{style:Qt.row,children:[me.jsx(hr,{style:[Qt.cellLabelContainer,{width:"25%"}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Lab. Director"})})
target_fragment = 'me.jsxs(hr,{style:Qt.row,children:[me.jsx(hr,{style:[Qt.cellLabelContainer,{width:"25%"}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Lab. Director"})})'
replacement_fragment = 'me.jsxs(hr,{style:[Qt.row,{borderBottomWidth:0}],children:[me.jsx(hr,{style:[Qt.cellLabelContainer,{width:"25%"}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Lab. Director"})})'

if target_fragment in content:
    new_content = content.replace(target_fragment, replacement_fragment)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully patched Lab Director table border.")
else:
    print("Error: Target Lab Director string not found. Check whitespace/syntax.")
    # Fallback debug: print nearby content if not found
    idx = content.find("Lab. Director")
    print("Nearby content:")
    print(content[idx-100:idx+200])
