
import os

base_dir = os.getcwd()
src_path = os.path.join(base_dir, 'assets', 'index-patched-31.js')
dest_path = os.path.join(base_dir, 'assets', 'index-patched-33.js')

print(f"Reading {src_path}")

with open(src_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Parsing Logic (Same as before)
target_parsing = 'U[Y("Lab Director")]'
replacement_parsing = 'U[Y("Lab. Director")]||U[Y("Lab Director")]'

if target_parsing in content:
    print("Applying parsing logic patch...")
    content = content.replace(target_parsing, replacement_parsing)
else:
    print("WARNING: Target parsing logic not found in index-patched-31.js!")

# 2. Update HTML Rendering (CORRECTED)
# Search for: children:g.inspector
# Replace with: children:C._inspector
# Context from verification: children:g.inspector})
target_html = 'children:g.inspector})'
replacement_html = 'children:C._inspector})'

if target_html in content:
    print(f"Applying HTML rendering patch (g.inspector -> C._inspector)...")
    content = content.replace(target_html, replacement_html)
else:
    print(f"WARNING: Target HTML rendering context '{target_html}' not found!")

print(f"Writing to {dest_path}")
with open(dest_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patching complete.")
