
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-10.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print("--- SAMPLE DATA (b=...) ---")
idx_b = content.find('b=()=>{p([')
if idx_b != -1:
    print(content[idx_b:idx_b+400])
else:
    print("Sample data function not found")

print("\n--- PARSING LOGIC (U._diabetic...) ---")
idx_p = content.find('U._diabetic=')
if idx_p != -1:
    print(content[idx_p-100:idx_p+300])
else:
    print("Parsing logic patch not found")

print("\n--- HTML LOGIC (Deterioration) ---")
# Search for the conditional logic I injected
# `children:((String(C._diabetic`
idx_h = content.find('String(C._diabetic')
if idx_h != -1:
    print(content[idx_h-100:idx_h+400])
else:
    print("HTML Conditional logic not found")
