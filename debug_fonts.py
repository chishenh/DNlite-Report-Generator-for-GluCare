
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

count = content.count('Helvetica')
print(f"Occurrences of 'Helvetica': {count}")

# Print unique variations relative to 'Helvetica' to see if there are 'Helvetica-Bold', etc.
import re
matches = re.findall(r'Helvetica[-\w]*', content)
unique_matches = set(matches)
print(f"Unique variations: {unique_matches}")
