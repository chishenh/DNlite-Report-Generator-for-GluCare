
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-7.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for "Lab. Director" or "Lab Director"
# Note: user wrote "Lab. Director"
start = 0
matches = []
while True:
    idx = content.find("Director", start)
    if idx == -1:
        break
    matches.append(idx)
    start = idx + 1

print(f"Found 'Director' at {matches}")
for idx in matches:
    print(f"--- Context {idx} ---")
    s = max(0, idx - 1000)
    e = min(len(content), idx + 1000)
    print(content[s:e])
