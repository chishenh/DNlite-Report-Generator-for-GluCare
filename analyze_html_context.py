
import os

base_dir = os.getcwd()
file_path = os.path.join(base_dir, 'assets', 'index-patched-31.js')

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

search_term = 'className:"text-xs text-slate-400 mb-2",children:"Lab. Director"'
idx = content.find(search_term)

if idx != -1:
    print(f"Found HTML block at {idx}")
    s = max(0, idx - 1000)
    e = min(len(content), idx + 1000)
    # Print with some formatting? No, just raw.
    print(content[s:e])
else:
    print("HTML block not found")
