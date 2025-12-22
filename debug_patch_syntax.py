
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-2.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('style:Qt.grid,children:[')
if idx != -1:
    print("Found patch start.")
    # Print the next 2000 chars to see the structure I injected
    print(content[idx:idx+2000])
else:
    print("Patch start NOT FOUND.")
