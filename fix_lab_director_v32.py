
import os

base_dir = os.getcwd()
file_path = os.path.join(base_dir, 'assets', 'index-patched-31.js')

print(f"Reading {file_path}")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Parsing Logic
# Search for: U[Y("Lab Director")]
# Replace with: U[Y("Lab. Director")]||U[Y("Lab Director")]
target_parsing = 'U[Y("Lab Director")]'
replacement_parsing = 'U[Y("Lab. Director")]||U[Y("Lab Director")]'

if target_parsing in content:
    print("Applying parsing logic patch...")
    content = content.replace(target_parsing, replacement_parsing)
else:
    print("WARNING: Target parsing logic not found! It might have been already patched.")

# 2. Update HTML Rendering
# Search for: children:g.inspector (specifically in the footer context)
# We need to be careful not to replace other occurrences if any.
# The context found earlier was:
# children:[me.jsx("div",{className:"text-xs text-slate-400 mb-2",children:"Lab. Director"}),me.jsx("div",{className:"font-serif text-xl italic text-slate-800 border-b border-slate-300 pb-1 px-2 inline-block min-w-[150px]",children:g.inspector})]
# Let's use a slightly larger context to be safe.

target_html = 'children:g.inspector})'
replacement_html = 'children:g._inspector})'

# Count occurrences
count = content.count(target_html)
print(f"Found {count} occurrences of '{target_html}'")

# Based on analysis, this pattern seems specific enough for the footer value which is inside a div, returning a JSX element ending with })] or similar.
# The context was: ...children:g.inspector})]...
# Wait, the exact string in analysis was: ...children:g.inspector})]...
# Let's try to be precise.

target_html_context = 'children:g.inspector})'
replacement_html_context = 'children:g._inspector})'

if target_html_context in content:
    print("Applying HTML rendering patch...")
    content = content.replace(target_html_context, replacement_html_context)
else:
    print("WARNING: Target HTML rendering context not found!")
    # Fallback to check simpler pattern if precise one fails, but safer to warn first.
    # checking 'children:g.inspector' alone might be risky if used elsewhere.
    # Let's check 'className:"text-xs text-slate-400 mb-2",children:"Lab. Director"' context roughly?
    # Actually, let's try the slightly broader "children:g.inspector" but constrained.
    pass

new_file_path = os.path.join(base_dir, 'assets', 'index-patched-32.js')
print(f"Writing to {new_file_path}")
with open(new_file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patching complete. Remember to update index.html to point to index-patched-32.js")
