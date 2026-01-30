
import os
import re

base_dir = os.getcwd()
file_path = os.path.join(base_dir, 'assets', 'index-patched-31.js')

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = 'className:"footer-section"'
footer_idx = content.find(target)

if footer_idx != -1:
    # Look in the preceding 2000 chars for _disp_dnlite usage
    s = max(0, footer_idx - 2000)
    e = footer_idx
    sub = content[s:e]
    
    # Regex to find Variable._disp_dnlite
    # matches like C._disp_dnlite or i._disp_dnlite
    match = re.search(r'([a-zA-Z0-9_]+)\._disp_dnlite', sub)
    if match:
        var_name = match.group(1)
        print(f"[FOUND] Variable used with ._disp_dnlite is: '{var_name}'")
    else:
        print("[FAIL] Could not find ._disp_dnlite usage near footer.")
else:
    print("Footer not found")
