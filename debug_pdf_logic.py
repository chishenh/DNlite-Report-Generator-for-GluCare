
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-11.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for "higher than that of a diabetic patient"
# This string exists in BOTH the original DM block and my conditional logic (in the "true" branch).
# So finding it works for both.
# I want to see the surrounding characters (to see if conditional exists).

start = 0
matches = []
while True:
    idx = content.find("higher than that of a diabetic patient", start)
    if idx == -1:
        break
    matches.append(idx)
    start = idx + 1

print(f"Found matches at {matches}")

for idx in matches:
    print(f"--- Context {idx} ---")
    s = max(0, idx - 500)
    e = min(len(content), idx + 500)
    print(content[s:e])
