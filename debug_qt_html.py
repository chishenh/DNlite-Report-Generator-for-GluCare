
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-15.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Dump Qt Styles
# Search for `Qt={`, but minified might be `const Qt={`.
idx_qt = content.find('const Qt={')
if idx_qt != -1:
    print("Found Qt definition at", idx_qt)
    print("--- Qt Styles ---")
    # Dump a chunk, hoping to catch barCol or chartBox
    print(content[idx_qt:idx_qt+3000])
else:
    print("Qt definition not found via 'const Qt={'. Trying 'var Qt={'.")
    idx_qt_var = content.find('var Qt={')
    if idx_qt_var != -1:
        print(content[idx_qt_var:idx_qt_var+3000])

# Dump HTML Table Logic
# Search for "DNlite level" headers in HTML
# Usually `className:"..."` vs `style:`.
# Search `children:"DNlite level"` was for PDF.
# HTML likely uses simple `<h3>` or `<div>`.
# Search `children:"Remark"` inside the HTML block?
# Finding "Remark" might match both PDF and HTML.
# PDF usage: `me.jsx(ur,{style:Qt.thText,children:"Remark"})` (Found in prev dump).
# HTML usage: likely `<th>Remark</th>` or similar.
# Let's search for "Remark" and look for context with classNames (HTML).

start = 0
print("\n--- Remark Occurrences ---")
while True:
    idx = content.find('Remark', start)
    if idx == -1:
        break
    context = content[idx-100:idx+200]
    # Filter for HTML: Look for className
    if 'className' in context or '</th>' in context or 'div' in context:
        print(f"Match at {idx} (Likely HTML):")
        print(context)
    start = idx + 1
