
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-3.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Look for 'backgroundColor:"white"'
matches = []
start = 0
while True:
    idx = content.find('backgroundColor:"white"', start)
    if idx == -1:
        break
    matches.append(idx)
    start = idx + 1

print(f"Found 'backgroundColor:\"white\"' at: {matches}")
for idx in matches:
    print(f"--- Context {idx} ---")
    start_ctx = max(0, idx - 50)
    end_ctx = min(len(content), idx + 50)
    print(content[start_ctx:end_ctx])
