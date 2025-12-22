
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-C1D2uKbX.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. PDF Background
# Search: style:[Qt.page,{backgroundColor:h}]
# Replace: style:[Qt.page,{backgroundColor:"#ffffff"}]
new_content = content.replace('style:[Qt.page,{backgroundColor:h}]', 'style:[Qt.page,{backgroundColor:"#ffffff"}]')

# 2. PDF Chart Background
# Search: chartBox:{backgroundColor:Br.slate225
# Replace: chartBox:{backgroundColor:"#f8fafc"
new_content = new_content.replace('chartBox:{backgroundColor:Br.slate225', 'chartBox:{backgroundColor:"#f8fafc"')

# 3. HTML Chart Background
# Search: style:{backgroundColor:"#dce3eb"},children:[me.jsx(Fm
# Replace: style:{backgroundColor:"#f8fafc"},children:[me.jsx(Fm
# Note: replace method replaces all occurrences, which is what we want here as both charts use this structure.
new_content = new_content.replace('style:{backgroundColor:"#dce3eb"},children:[me.jsx(Fm', 'style:{backgroundColor:"#f8fafc"},children:[me.jsx(Fm')

if content == new_content:
    print("No changes made. Patterns not found.")
else:
    # Save as new file to cache bust
    new_file_path = file_path.replace('index-C1D2uKbX.js', 'index-patched.js')
    with open(new_file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully patched and saved to {new_file_path}")
