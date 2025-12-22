
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-17.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print("--- Usages of E3e (Gauge) ---")
start = 0
while True:
    idx = content.find('jsx(E3e', start) # Search jsx usage
    if idx == -1:
        # Try variable usage
        idx = content.find('E3e(', start) # Direct call?
        if idx == -1:
            break
    print(f"Match at {idx}:")
    print(content[idx-100:idx+200])
    start = idx + 1

print("\n--- Usages of Fm (Bar) ---")
start = 0
while True:
    idx = content.find('jsx(Fm', start)
    if idx == -1:
        break
    print(f"Match at {idx}:")
    print(content[idx-100:idx+200])
    start = idx + 1
