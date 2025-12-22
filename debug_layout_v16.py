
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-15.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# PDF Table: "DNlite level"
# Headers: "Item", "Value", "Unit", "Reference Interval", "Remark"
idx_table = content.find('children:"DNlite level"')
if idx_table != -1:
    print("Found 'DNlite level' at", idx_table)
    print("--- Context Table ---")
    print(content[idx_table:idx_table+3000]) # Need large context to see col rendering loop
else:
    print("Error: 'DNlite level' not found.")

# HTML Charts: "Renal Function Deterioration"
# Look for the HTML block
idx_html = content.find('children:((String(C._diabetic') # Use my injected string to find the exact block
if idx_html != -1:
    print("\nFound HTML Logic Block at", idx_html)
    print("--- Context HTML ---")
    print(content[idx_html:idx_html+2000])
else:
    print("Error: HTML logic block not found.")
