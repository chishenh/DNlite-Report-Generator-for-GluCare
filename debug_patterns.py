
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-C1D2uKbX.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File length: {len(content)}")

# Diagnostic for chartBox
idx = content.find('chartBox')
if idx != -1:
    print(f"Found chartBox at {idx}")
    print(f"Snippet: {content[idx:idx+100]}")
else:
    print("chartBox NOT FOUND")

# Diagnostic for Qt.page
idx2 = content.find('Qt.page')
if idx2 != -1:
    print(f"Found Qt.page at {idx2}")
    print(f"Snippet: {content[idx2:idx2+100]}")
else:
    print("Qt.page NOT FOUND")
