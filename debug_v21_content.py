
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-21.js'

if not os.path.exists(file_path):
    print(f"File {file_path} not found.")
else:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Search for b3e
    idx = content.find('b3e=')
    if idx != -1:
        print(f"Found b3e at {idx}")
        print("--- Context Around b3e in v21 ---")
        print(content[idx-200:idx+2000])
    else:
        print("b3e not found in v21.")

    # Check Fm
    idx_fm = content.find('Fm=')
    if idx_fm != -1:
        print(f"\nFound Fm at {idx_fm}")
        print(content[idx_fm:idx_fm+200])

    # Search for any obvious syntax errors I might have introduced
    # e.g. double semicolons, mismatched brackets near patch join
    # Join point 1: before b3e
    # Join point 2: after b3e
