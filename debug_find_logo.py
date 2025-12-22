
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-6.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for likely HTML structure
# "Test Report" is in the header.
# Look for 'img' tags nearby.
# Since it's React/JSX, looks like me.jsx('img', {src: ...})

# We want the HTML preview, not the PDF PDF uses 'dh' (Image) component usually.
# HTML preview usually uses 'img' or 'div' with background.

# Search for "Test Report"
start = 0
while True:
    idx = content.find("Test Report", start)
    if idx == -1:
        break
    
    # Print context
    print(f"--- MATCH at {idx} ---")
    s = max(0, idx - 1000)
    e = min(len(content), idx + 1000)
    print(content[s:e])
    
    start = idx + 1
