
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-2.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for "Qt={" or "Qt = {" or just "cellLabelContainer:"
# Since it's minified, it might be "var Qt={...}" or "const Qt={...}" or just "Qt={...}"
# Let's search for "cellLabelContainer:" and look backwards for "Qt={"
idx = content.find("cellLabelContainer:")
if idx != -1:
    print(f"Found cellLabelContainer at {idx}")
    start = max(0, idx - 1000)
    end = min(len(content), idx + 1000)
    print("--- Context ---")
    print(content[start:end])
else:
    print("cellLabelContainer NOT FOUND")
