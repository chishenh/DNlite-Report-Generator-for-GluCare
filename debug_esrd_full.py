
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-8.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate "End-Stage Renal Disease (ESRD)"
idx_esrd = content.find("End-Stage Renal Disease (ESRD)")

if idx_esrd != -1:
    print(f"--- ESRD Context ---")
    start = idx_esrd
    end = start + 800
    print(content[start:end])
else:
    print("ESRD section title not found")
