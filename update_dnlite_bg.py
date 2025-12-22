
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-5.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Target from debug check: matches 3 times, corresponding to the 3 rows.
target_str = 'style:[Qt.tdContainer,{width:"35%",backgroundColor:Br.slate225}]'
replacement_str = 'style:[Qt.tdContainer,{width:"35%",backgroundColor:"#f8fafc"}]'

new_content = content.replace(target_str, replacement_str)

if new_content == content:
    print("Error: No replacements made.")
else:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully replaced background color in {file_path}")
