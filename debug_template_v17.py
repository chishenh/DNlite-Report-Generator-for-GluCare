
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-16.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for Template Generation
# Keywords: "xlsx", "book_new", "aoa_to_sheet", "Sampling Date" (header usage)
# The sample data headers I dumped earlier: `["姓名","Age","Gender","Clinic","Sampling Date","MRN","uPTM-FetA","UCr"]`
# I should look for *another* occurrence of this array, or where it's used for writing.

print("--- Searching for Headers Array ---")
# Shortened search string to avoid whitespace issues
header_sig = '"Sampling Date","MRN"'
start = 0
while True:
    idx = content.find(header_sig, start)
    if idx == -1:
        break
    print(f"Match at {idx}:")
    print(content[idx-100:idx+300])
    start = idx + 1

# Search for Chart Width 96
print("\n--- Searching for Width 96 ---")
width_sig = 'style:{width:96,height:'
idx_w = content.find(width_sig)
if idx_w != -1:
    print(f"Found Width 96 at {idx_w}")
    print(content[idx_w:idx_w+200])
