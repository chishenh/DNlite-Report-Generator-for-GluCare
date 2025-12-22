
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-9.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for "9.5 times"
# Usage 1: PDF component (already patched?)
# Usage 2: HTML Component

start = 0
matches = []
while True:
    idx = content.find("9.5 times", start)
    if idx == -1:
        break
    matches.append(idx)
    start = idx + 1

print(f"Found '9.5 times' at {matches}")

for idx in matches:
    print(f"--- Context {idx} ---")
    s = max(0, idx - 500)
    e = min(len(content), idx + 500)
    print(content[s:e])
