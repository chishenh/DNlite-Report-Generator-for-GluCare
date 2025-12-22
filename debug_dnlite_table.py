
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-3.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for "DNlite Level" section title
start_str = 'children:"DNlite Level"})]}),'
idx_start = content.find(start_str)

if idx_start != -1:
    print(f"Found start at {idx_start}")
    # Print next 3000 chars to cover the table logic
    print(content[idx_start:idx_start+3000])
else:
    print("Start string not found")
