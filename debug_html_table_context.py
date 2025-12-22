
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-17.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for HTML Header: th with DNlite
# Logic: `jsx("th",` ... `children:"DNlite`
start = 0
found = False
while True:
    idx = content.find('jsx("th",', start)
    if idx == -1:
        break
    # Checking if DNlite is close
    sub = content[idx:idx+300]
    if 'DNlite' in sub:
        print(f"Found HTML DNlite Table Header at {idx}")
        # Dump larger context to find END of TABLE
        print("--- HTML Table Context ---")
        print(content[idx:idx+4000])
        found = True
        break
    start = idx + 1

if not found:
    print("HTML DNlite Table Header not found via 'jsx(\"th\",'.")
