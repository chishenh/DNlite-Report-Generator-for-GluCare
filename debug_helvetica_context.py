
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find occurrences of "Helvetica" and print surrounding characters
# to identify if it's in a map like { Helvetica: ... }
import re
# Look for property keys or values
matches = [m.start() for m in re.finditer(r'"Helvetica"', content)]

for i in matches[:5]: # just first 5
    start = max(0, i - 100)
    end = min(len(content), i + 200)
    print(f"--- Match at {i} ---")
    print(content[start:end])
    print("--------------------")

# Check for ReactPDF specific keywords
print(f"hyphenationCallback found: {'hyphenationCallback' in content}")
print(f".register found: {'.register' in content}")
