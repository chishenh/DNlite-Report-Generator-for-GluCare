
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-23.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the exact style strings to be precise.
# Pattern: height:"10%" -> height:8, etc.

replacements = [
    ('height:"10%"', 'height:8'),
    ('height:"95%"', 'height:76'),
    ('height:"40%"', 'height:32'),
    ('height:"35%"', 'height:28'),
    ('height:"16%"', 'height:13')
]

for old, new in replacements:
    content = content.replace(old, new)
    print(f"Replaced {old} with {new}")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
