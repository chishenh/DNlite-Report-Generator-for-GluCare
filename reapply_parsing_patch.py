
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-10.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Target Parsing Logic
# It seems the previous patch was lost.
# Search for `U._unit=`
# We want: `U._diabetic=U[Y("Diabetic")]||"Yes",U._unit=`

# Current state likely: `...,U._unit=U[Y("單位")]...`
target_parse_fragment = 'U._unit=U[Y("單位")]'
repl_parse_fragment = 'U._diabetic=U[Y("Diabetic")]||"Yes",U._unit=U[Y("單位")]'

if target_parse_fragment in content:
    # Check if already applied? (The debug script said not found, so presumably not applied)
    if 'U._diabetic=' in content:
        print("U._diabetic already present? (Weird logic)")
    else:
        content = content.replace(target_parse_fragment, repl_parse_fragment)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully re-applied Parsing Patch.")
else:
    print("Error: Parsing target not found.")
    # Debug context
    idx = content.find("U._unit")
    if idx != -1:
        print("Context found:")
        print(content[idx-50:idx+50])
