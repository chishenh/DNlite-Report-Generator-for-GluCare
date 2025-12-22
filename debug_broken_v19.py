
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-19.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for b3e
idx = content.find('b3e=')
if idx != -1:
    print(f"Found b3e at {idx}")
    print("--- Context Around b3e ---")
    # Show before and AFTER the patch to see the join point
    print(content[idx-100:idx+2000])
else:
    print("b3e not found in v19 (Maybe patch failed/renamed?)")
