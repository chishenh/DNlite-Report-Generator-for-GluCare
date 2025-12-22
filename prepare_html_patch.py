
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-9.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Helper Logic for HTML
# Variable `C` is the row object in HTML loop (from dump 2248825: `r.map((C,T)=>`).
dm_check_html = '(String(C._diabetic||"YES").toUpperCase()!=="NO")'

# --- HTML Patch 1: Deterioration Text ---
# Target: `children:["If your DNlite level is ",me.jsx("span",{className:"font-bold",style:{color:V0.red},children:"High Risk"}),", your risk of renal function deterioration within 5 years is ",me.jsx("span",{className:"font-bold text-sm",style:{color:V0.red},children:"9.5 times"})," higher than that of a diabetic patient."]`
# Non-DM: "... 4.0 times ... general population."

target_html_det = 'children:["If your DNlite level is ",me.jsx("span",{className:"font-bold",style:{color:V0.red},children:"High Risk"}),", your risk of renal function deterioration within 5 years is ",me.jsx("span",{className:"font-bold text-sm",style:{color:V0.red},children:"9.5 times"})," higher than that of a diabetic patient."]'

non_dm_html_det = '["If your DNlite level is ",me.jsx("span",{className:"font-bold",style:{color:V0.red},children:"High Risk"}),", your risk of renal function deterioration within 5 years is ",me.jsx("span",{className:"font-bold text-sm",style:{color:V0.red},children:"4.0 times"})," higher than that of the general population."]'

repl_html_det = f'children:({dm_check_html} ? {target_html_det[9:]} : {non_dm_html_det})'

if target_html_det in content:
    content = content.replace(target_html_det, repl_html_det)
    print("HTML Patch 1 (Deterioration) applied.")
else:
    print("Error: HTML Patch 1 target not found.")

# --- HTML Patch 2: Deterioration Chart ---
# Target: `me.jsx(Fm,{value:9.5,label:"High Risk",color:V0.red})`
# Replace 9.5 with conditional.
target_chart_det = 'me.jsx(Fm,{value:9.5,label:"High Risk",color:V0.red})'
repl_chart_det = f'me.jsx(Fm,{{value:{dm_check_html}?9.5:4.0,label:"High Risk",color:V0.red}})'

if target_chart_det in content:
    content = content.replace(target_chart_det, repl_chart_det)
    print("HTML Patch 2 (Deterioration Chart) applied.")
else:
    print("Error: HTML Patch 2 target not found.")


# --- HTML Patch 3: ESRD Text ---
# Assuming similar structure to Deterioration but with 3.5 / 1.6.
# I need to verify the exact string. Dump 2257044 cut off before ESRD.
# I will use a generic search-replace for the ESRD number unique context if possible, or dump it first?
# "risk of developing ESRD within 5 years is" ... "3.5 times"
# I should probably dump it to be safe. But "3.5 times" logic is identical to PDF.
# Let's try to construct it blindly based on PDF pattern: 
# `children:["If you are categorized as ",me.jsx("span",{...children:"High Risk"}),", your risk of developing ESRD within 5 years is ",me.jsx("span",{...children:"3.5 times"})," higher than that of a diabetic patient."]`
# Note: HTML uses `span` and `className`, PDF uses `ur` and `style`.

# I will skip applying Patch 3 blindly. I will find it first.
# Writing partial modifications for now. I'll read and rewrite.

with open('c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/debug_html_esrd.py', 'w', encoding='utf-8') as debug_f:
    debug_f.write("""
import os
with open('c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-9.js', 'r', encoding='utf-8') as f:
    c = f.read()
idx = c.find("developing ESRD within 5 years is")
if idx != -1:
    print("--- HTML ESRD ---")
    print(c[idx-200:idx+600])
""")

with open('c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/update_dm_logic_html_partial.py', 'w', encoding='utf-8') as f:
    f.write(content) # NO, this writes the whole JS file to python script. BAD.
    
# Correct approach: Write the patching script. But I need the ESRD string.
# I will output a script that does Patch 1 & 2, and prints if they worked. 
# And I'll run the debug script separately.
