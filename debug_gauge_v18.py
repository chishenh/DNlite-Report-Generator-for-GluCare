
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-17.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print("--- Searching for Gauge Values ---")
values = ["7.53", "300"]
for v in values:
    idx = content.find(v)
    if idx != -1:
        print(f"Found {v} at {idx}")
        print(content[idx-200:idx+200])
    else:
        print(f"{v} not found.")

# Also search for 'gradient' to find the visual
idx_grad = content.find('linear-gradient')
if idx_grad != -1:
    print(f"\nFound linear-gradient at {idx_grad}")
    print(content[idx_grad-200:idx_grad+300])
