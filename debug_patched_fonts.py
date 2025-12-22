
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('Hanken Grotesk')
if idx != -1:
    print(f"Found 'Hanken Grotesk' at {idx}")
    print(f"Context: {content[idx:idx+50]}")
    
    # Check for "Bold"
    idx_bold = content.find('Hanken Grotesk-Bold')
    if idx_bold != -1:
        print("Found 'Hanken Grotesk-Bold' explicitly.")
    else:
        print("'Hanken Grotesk-Bold' NOT found.")
        
    # Check for what *is* there where Helvetica-Bold used to be
    # Assuming there are multiple occurrences
    import re
    matches = re.findall(r'Hanken Grotesk.{0,20}', content)
    print("Sample matches:", matches[:10])
else:
    print("'Hanken Grotesk' NOT FOUND in file.")
