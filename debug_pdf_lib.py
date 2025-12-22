
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Look for patterns like register({family: ...})
# or just any object that looks like encoding a font.
# react-pdf structure: Font.register({ family: 'Oswald', src: '...' });

# Since 'Font.register' failed, maybe just search for 'register' and inspect context?
# But 'register' is common.

# Let's search for "Times-Roman" or "Helvetica" to see if there's a default list.
# We already replaced Helvetica... so search for "Hanken Grotesk" to see context.

idx = content.find("Hanken Grotesk")
if idx != -1:
    print(f"snippet around first Hanken Grotesk: {content[idx-50:idx+150]}")

# Identifying the library
if "react-pdf" in content:
    print("Found 'react-pdf' string.")
elif "jspdf" in content:
    print("Found 'jspdf' string.")
elif "pdfkit" in content:
    print("Found 'pdfkit' string.")
else:
    print("Could not identify PDF library string.")
