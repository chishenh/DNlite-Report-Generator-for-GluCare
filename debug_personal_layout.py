
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for "Personal"
match_indices = []
start = 0
while True:
    idx = content.find("Personal", start)
    if idx == -1:
        break
    match_indices.append(idx)
    start = idx + 1

print(f"Found 'Personal' at indices: {match_indices}")

for idx in match_indices:
    # Print context
    print(f"--- Context at {idx} ---")
    start_ctx = max(0, idx - 200)
    end_ctx = min(len(content), idx + 1000) # Get a good chunk to see the table structure
    print(content[start_ctx:end_ctx])
    print("------------------------")
