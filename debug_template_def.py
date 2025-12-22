
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-16.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

idx_template = content.find('DNlite_Report_Template.xlsx')
if idx_template != -1:
    print("Found template name at", idx_template)
    # Dump BEFORE to find definition of k (header data)
    print("--- Pre-Context Template ---")
    print(content[idx_template-500:idx_template])
    
# also check for strings like headers but NOT in the `p` function
headers = '["姓名","Age"'
start = 0
while True:
    idx = content.find(headers, start)
    if idx == -1:
        break
    # Exclude if it looks like `p([["姓名"` (Sample load)
    # Check surrounding
    surrounding = content[idx-10:idx+len(headers)+10]
    print(f"Found headers at {idx}: {surrounding}")
    start = idx + 1
