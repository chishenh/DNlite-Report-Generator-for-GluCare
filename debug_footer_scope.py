
import os

base_dir = os.getcwd()
file_path = os.path.join(base_dir, 'assets', 'index-patched-32.js')

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = 'className:"footer-section"'
idx = content.find(target)

if idx != -1:
    print(f"Found footer at {idx}")
    # Get 2000 chars BEFORE the footer to see what variables are used
    s = max(0, idx - 2000)
    e = idx + 200
    print("--- Footer Preceding Context ---")
    print(content[s:e])
else:
    print("Footer not found")
