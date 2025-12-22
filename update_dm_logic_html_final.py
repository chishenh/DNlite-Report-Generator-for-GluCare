
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-9.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Helper Logic matching HTML loop
dm_check_html = '(String(C._diabetic||"YES").toUpperCase()!=="NO")'

# --- HTML Patch 1 & 2 (Deterioration) ---
# (Repeated here to ensure complete file, or assume prepare_html_patch was run? 
# I will re-run replacement logic. If already replaced, it won't match target, so it's safe if robust.)
# BUT my `prepare_html_patch.py` printed "Applied". It did NOT save? 
# Wait, `prepare_html_patch.py` does `content.replace` but did NOT write to file!
# I checked the code for `prepare_html_patch.py`:
# `with open(..., 'w') as f: f.write(content)` was NOT present.
# Ah, I see `with open(...) as debug_f` then `with open(...) as f: f.write(content)`.
# Wait, I wrote `prepare_html_patch.py` content to file `prepare_html_patch.py`.
# Did I execute it? Yes.
# Did it have `f.write(content)`?
# Let's check the code I wrote in previous turn (Step 436).
# `with open('.../debug_html_esrd.py', 'w')`...
# `with open('.../update_dm_logic_html_partial.py', 'w') as f: f.write(content)`
# Wait, I wrote the *content of JS* to a python file `update_dm_logic_html_partial.py`?
# NO.
# I wrote a python script `prepare_html_patch.py` that imports os, reads file, does replacements...
# AND `with open(..., 'w') as f: f.write(content)` WAS MISSING in my thought process?
# Let's look at Step 436 code:
# `content = f.read()`
# `repl_chart_det = ...`
# `content = content.replace(...)`
# `print("HTML Patch 2 ... applied.")`
# ...
# `with open('.../debug_html_esrd.py', 'w')`...
# `with open('.../update_dm_logic_html_partial.py', 'w')`...
# It seemed to write the *JS content* to a python file? No, I stopped myself.
# BUT I did NOT write the modified content back to `index-patched-9.js`.
# Checking output of Step 437: "HTML Patch 1 ... applied."
# But no "Successfully wrote..." message.
# So `index-patched-9.js` is UNMODIFIED.
# Good. I can include all patches in `update_dm_logic_html_final.py`.

# --- DEFINITIONS ---
target_html_det = 'children:["If your DNlite level is ",me.jsx("span",{className:"font-bold",style:{color:V0.red},children:"High Risk"}),", your risk of renal function deterioration within 5 years is ",me.jsx("span",{className:"font-bold text-sm",style:{color:V0.red},children:"9.5 times"})," higher than that of a diabetic patient."]'

non_dm_html_det = '["If your DNlite level is ",me.jsx("span",{className:"font-bold",style:{color:V0.red},children:"High Risk"}),", your risk of renal function deterioration within 5 years is ",me.jsx("span",{className:"font-bold text-sm",style:{color:V0.red},children:"4.0 times"})," higher than that of the general population."]'

repl_html_det = f'children:({dm_check_html} ? {target_html_det[9:]} : {non_dm_html_det})'


target_chart_det = 'me.jsx(Fm,{value:9.5,label:"High Risk",color:V0.red})'
repl_chart_det = f'me.jsx(Fm,{{value:{dm_check_html}?9.5:4.0,label:"High Risk",color:V0.red}})'


# --- ESRD Logic ---
# Need to find HTML ESRD string. 
# Search for `children:"3.5 times"` starting from end of file backwards? Or just split logic.
# I will use a regex-like finder or just exact string match if possible.
# Unique enough: `children:"3.5 times",` followed by `higher than that of a diabetic patient`
# AND using `className` or `V0.red`.
# Let's guess the string based on Deterioration pattern.
# Deterioration: `me.jsx("span",{className:"font-bold text-sm",style:{color:V0.red},children:"9.5 times"})`
# ESRD likely: `me.jsx("span",{className:"font-bold text-sm",style:{color:V0.red},children:"3.5 times"})`
# Let's verify existence.

search_esrd = 'me.jsx("span",{className:"font-bold text-sm",style:{color:V0.red},children:"3.5 times"})'
if search_esrd in content:
    print("Found HTML ESRD fragment.")
    # Now construct the full block replacement
    target_html_esrd = 'children:["If you are categorized as ",me.jsx("span",{className:"font-bold",style:{color:V0.red},children:"High Risk"}),", your risk of developing ESRD within 5 years is ",me.jsx("span",{className:"font-bold text-sm",style:{color:V0.red},children:"3.5 times"})," higher than that of a diabetic patient."]'
    
    non_dm_html_esrd = '["If you are categorized as ",me.jsx("span",{className:"font-bold",style:{color:V0.red},children:"High Risk"}),", your risk of developing ESRD within 5 years is ",me.jsx("span",{className:"font-bold text-sm",style:{color:V0.red},children:"1.6 times"})," higher than that of the general population."]'

    repl_html_esrd = f'children:({dm_check_html} ? {target_html_esrd[9:]} : {non_dm_html_esrd})'
    
    if target_html_esrd in content:
        content = content.replace(target_html_esrd, repl_html_esrd)
        print("HTML Patch 3 (ESRD) applied.")
    else:
        print("Error: Full HTML ESRD block not found (Fragment found but full string mismatch?)")
        # Debugging: print context around fragment
        idx = content.find(search_esrd)
        print("Context around found fragment:")
        print(content[idx-100:idx+300])

else:
    print("Error: HTML ESRD fragment not found.")

# --- ESRD Chart ---
target_chart_esrd = 'me.jsx(Fm,{value:3.5,label:"High Risk",color:V0.red})'
repl_chart_esrd = f'me.jsx(Fm,{{value:{dm_check_html}?3.5:1.6,label:"High Risk",color:V0.red}})'

if target_chart_esrd in content:
    content = content.replace(target_chart_esrd, repl_chart_esrd)
    print("HTML Patch 4 (ESRD Chart) applied.")
else:
    print("Error: HTML Patch 4 target not found.")

# Apply Patches 1 & 2
if target_html_det in content:
    content = content.replace(target_html_det, repl_html_det)
    print("HTML Patch 1 (Deterioration) applied.")

if target_chart_det in content:
    content = content.replace(target_chart_det, repl_chart_det)
    print("HTML Patch 2 (Deterioration Chart) applied.")

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("File updated.")
