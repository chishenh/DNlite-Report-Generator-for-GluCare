
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-8.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Excel Parsing Context
# Search for `U[Y("Age")]`
idx_parse = content.find('U[Y("Age")]')
if idx_parse != -1:
    print(f"--- Excel Parsing Parsing at {idx_parse} ---")
    print(content[idx_parse-200:idx_parse+600])

# 2. Risk Definition Text
# Search for "9.5 times"
idx_risk_def = content.find("9.5 times")
if idx_risk_def != -1:
    print(f"--- Risk Definition Text at {idx_risk_def} ---")
    print(content[idx_risk_def-300:idx_risk_def+500])

# 3. Risk Mark Text (Appears in 'Important Notes'?)
# Search for "Your kidney function is within the normal range"
# This might appear multiple times.
idx_risk_mark = content.find("Your kidney function is within the normal range")
if idx_risk_mark != -1:
    print(f"--- Risk Mark Text at {idx_risk_mark} ---")
    print(content[idx_risk_mark-200:idx_risk_mark+500])
