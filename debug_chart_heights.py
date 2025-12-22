
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-14.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for Non-DM ESRD Value "1.6"
idx = content.find('children:"1.6"')
if idx != -1:
    print("Found 'children:\"1.6\"' at index", idx)
    print("--- Context ---")
    print(content[idx-100:idx+400])
else:
    print("Error: 'children:\"1.6\"' not found.")
    
# Debug: Search for "4.0" to compare
idx2 = content.find('children:"4.0"')
if idx2 != -1:
    print("\nFound 'children:\"4.0\"' at index", idx2)
    print("--- Context ---")
    print(content[idx2-100:idx2+400])
