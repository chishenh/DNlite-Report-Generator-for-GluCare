
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Revert "Hanken Grotesk" to "Helvetica"
# This reverses the previous patch.
new_content = content.replace('Hanken Grotesk', 'Helvetica')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Reverted fonts in {file_path}")
