
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-11.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Helper Logic
# `i` is the row object in Uk component map function (confirmed by dump `a.map((i,s)=>`).
dm_check_pdf = '(String(i._diabetic||"YES").toUpperCase()!=="NO")'

# --- PDF Patch 1: Deterioration Text ---
# Target: `children:["If your DNlite level is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"High Risk"}),", your risk of renal function deterioration within 5 years is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"9.5 times"})," higher than that of a diabetic patient."]`
# Non-DM: "... 4.0 times ... general population."

target_pdf_det = 'children:["If your DNlite level is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"High Risk"}),", your risk of renal function deterioration within 5 years is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"9.5 times"})," higher than that of a diabetic patient."]'

non_dm_pdf_det = '["If your DNlite level is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"High Risk"}),", your risk of renal function deterioration within 5 years is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"4.0 times"})," higher than that of the general population."]'

repl_pdf_det = f'children:({dm_check_pdf} ? {target_pdf_det[9:]} : {non_dm_pdf_det})'

if target_pdf_det in content:
    content = content.replace(target_pdf_det, repl_pdf_det)
    print("PDF Patch 1 (Deterioration) applied.")
else:
    print("Error: PDF Patch 1 target not found.")

# --- PDF Patch 2: Deterioration Chart ---
# Target: `children:[me.jsx(ur,{style:[Qt.barVal,{color:Br.red}],children:"9.5"}),me.jsx(hr,{style:{width:60,height:"95%",backgroundColor:Br.red,borderTopLeftRadius:2,borderTopRightRadius:2}}),me.jsx(ur,{style:Qt.barLabel,children:"High"})]`
# Wait, the dump 2233973 shows `children:"9.5"` is separate from `height:"95%"`.
# I should patch both if possible, or key off the value.
# Non-DM: 4.0 times is ~40% relative to diabetic? No, chart scale.
# If 9.5 is height 95%, then 4.0 is maybe height 40%? Or is it fixed scale?
# The dump shows `height:"95%"`.
# I should make them conditional. `children: (isDM ? "9.5" : "4.0")`.
# `height: (isDM ? "95%" : "40%")`.
# This is complex string replacement.
# Let's replace the whole `children:[me.jsx(ur,{style:[Qt.barVal,{color:Br.red} ... children:"High"})]` block with a conditional block.

target_pdf_det_chart = 'children:[me.jsx(ur,{style:[Qt.barVal,{color:Br.red}],children:"9.5"}),me.jsx(hr,{style:{width:60,height:"95%",backgroundColor:Br.red,borderTopLeftRadius:2,borderTopRightRadius:2}}),me.jsx(ur,{style:Qt.barLabel,children:"High"})]'

non_dm_pdf_det_chart = 'children:[me.jsx(ur,{style:[Qt.barVal,{color:Br.red}],children:"4.0"}),me.jsx(hr,{style:{width:60,height:"40%",backgroundColor:Br.red,borderTopLeftRadius:2,borderTopRightRadius:2}}),me.jsx(ur,{style:Qt.barLabel,children:"High"})]'

# Logic: `children: (isDM ? [DM_ARR] : [NON_DM_ARR])`.
repl_pdf_det_chart = f'children:({dm_check_pdf} ? {target_pdf_det_chart[9:]} : {non_dm_pdf_det_chart[9:]})'

if target_pdf_det_chart in content:
    content = content.replace(target_pdf_det_chart, repl_pdf_det_chart)
    print("PDF Patch 2 (Deterioration Chart) applied.")
else:
    print("Error: PDF Patch 2 target not found.")


# --- PDF Patch 3: ESRD Text ---
target_pdf_esrd = 'children:["If you are categorized as ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"High Risk"}),", your risk of developing ESRD within 5 years is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"3.5 times"})," higher than that of a diabetic patient."]'

non_dm_pdf_esrd = '["If you are categorized as ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"High Risk"}),", your risk of developing ESRD within 5 years is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"1.6 times"})," higher than that of the general population."]'

repl_pdf_esrd = f'children:({dm_check_pdf} ? {target_pdf_esrd[9:]} : {non_dm_pdf_esrd})'

if target_pdf_esrd in content:
    content = content.replace(target_pdf_esrd, repl_pdf_esrd)
    print("PDF Patch 3 (ESRD) applied.")
else:
    print("Error: PDF Patch 3 target not found.")

# --- PDF Patch 4: ESRD Chart ---
# ESRD Chart values: 3.5 (Diabetic) vs 1.6 (Non-DM).
# Current styling from dump 2235236:
# `children:[me.jsx(ur,{style:[Qt.barVal,{color:Br.red}],children:"3.5"}),me.jsx(hr,{style:{width:60,height:"95%",backgroundColor:Br.red, ...`
# Wait, ESRD 3.5 is ALSO height 95%?
# If so, 1.6 should be roughly 43% (1.6/3.5 * 95). Let's use 43%.

target_pdf_esrd_chart = 'children:[me.jsx(ur,{style:[Qt.barVal,{color:Br.red}],children:"3.5"}),me.jsx(hr,{style:{width:60,height:"95%",backgroundColor:Br.red,borderTopLeftRadius:2,borderTopRightRadius:2}}),me.jsx(ur,{style:Qt.barLabel,children:"High"})]'

non_dm_pdf_esrd_chart = 'children:[me.jsx(ur,{style:[Qt.barVal,{color:Br.red}],children:"1.6"}),me.jsx(hr,{style:{width:60,height:"43%",backgroundColor:Br.red,borderTopLeftRadius:2,borderTopRightRadius:2}}),me.jsx(ur,{style:Qt.barLabel,children:"High"})]'

repl_pdf_esrd_chart = f'children:({dm_check_pdf} ? {target_pdf_esrd_chart[9:]} : {non_dm_pdf_esrd_chart[9:]})'

if target_pdf_esrd_chart in content:
    content = content.replace(target_pdf_esrd_chart, repl_pdf_esrd_chart)
    print("PDF Patch 4 (ESRD Chart) applied.")
else:
    print("Error: PDF Patch 4 target not found.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("PDF patches re-applied.")
