
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-8.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate "9.5 times" (Deterioration) again
idx_deg = content.find("9.5 times")

# Look ahead for ESRD / "3.5 times"
if idx_deg != -1:
    print(f"--- Context after 9.5 times (looking for ESRD) ---")
    print(content[idx_deg:idx_deg+1200]) # Enough to cover the next section
else:
    print("Could not find '9.5 times'")
