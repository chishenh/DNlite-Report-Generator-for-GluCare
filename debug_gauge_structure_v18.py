
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-17.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Dump E3e component
# Search `E3e=({value:e`
idx_e3e = content.find('E3e=({value:e')
if idx_e3e != -1:
    print("Found E3e at", idx_e3e)
    # Dump enough to see the returned JSX
    print(content[idx_e3e:idx_e3e+2000])
