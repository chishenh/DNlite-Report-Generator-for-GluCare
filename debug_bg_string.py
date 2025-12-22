
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-5.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target_str = 'style:[Qt.tdContainer,{width:"35%",backgroundColor:Br.slate225}]'
count = content.count(target_str)

print(f"Target string found {count} times.")
if count > 0:
    print("Example context:")
    idx = content.find(target_str)
    print(content[idx:idx+100])
