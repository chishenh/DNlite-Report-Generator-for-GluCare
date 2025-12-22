
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-12.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Helper Logic matching PDF logic
# `i` is the row object (from map `a.map((i,s)=>`).
dm_check_pdf = '(String(i._diabetic||"YES").toUpperCase()!=="NO")'

# --- PDF Patch 1: Deterioration Text ---
target_pdf_det = 'children:["If your DNlite level is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"High Risk"}),", your risk of renal function deterioration within 5 years is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"9.5 times"})," higher than that of a diabetic patient."]'
non_dm_pdf_det = '["If your DNlite level is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"High Risk"}),", your risk of renal function deterioration within 5 years is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"4.0 times"})," higher than that of the general population."]'
repl_pdf_det = f'children:({dm_check_pdf} ? {target_pdf_det[9:]} : {non_dm_pdf_det})'

# --- PDF Patch 2: Deterioration Chart ---
# Height logic: DM 9.5 -> 95%. Non-DM 4.0 -> 40%.
target_pdf_det_chart = 'children:[me.jsx(ur,{style:[Qt.barVal,{color:Br.red}],children:"9.5"}),me.jsx(hr,{style:{width:60,height:"95%",backgroundColor:Br.red,borderTopLeftRadius:2,borderTopRightRadius:2}}),me.jsx(ur,{style:Qt.barLabel,children:"High"})]'
non_dm_pdf_det_chart = 'children:[me.jsx(ur,{style:[Qt.barVal,{color:Br.red}],children:"4.0"}),me.jsx(hr,{style:{width:60,height:"40%",backgroundColor:Br.red,borderTopLeftRadius:2,borderTopRightRadius:2}}),me.jsx(ur,{style:Qt.barLabel,children:"High"})]'
repl_pdf_det_chart = f'children:({dm_check_pdf} ? {target_pdf_det_chart[9:]} : {non_dm_pdf_det_chart[9:]})'

# --- PDF Patch 3: ESRD Text ---
target_pdf_esrd = 'children:["If you are categorized as ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"High Risk"}),", your risk of developing ESRD within 5 years is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"3.5 times"})," higher than that of a diabetic patient."]'
non_dm_pdf_esrd = '["If you are categorized as ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"High Risk"}),", your risk of developing ESRD within 5 years is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"1.6 times"})," higher than that of the general population."]'
repl_pdf_esrd = f'children:({dm_check_pdf} ? {target_pdf_esrd[9:]} : {non_dm_pdf_esrd})'

# --- PDF Patch 4: ESRD Chart ---
# Height logic: DM 3.5 -> 35% (Was 95% in original file). Non-DM 1.6 -> 16%.
# Note: Original code had `height:"95%"` for 3.5. We are changing this to match HTML (35%).

target_pdf_esrd_chart = 'children:[me.jsx(ur,{style:[Qt.barVal,{color:Br.red}],children:"3.5"}),me.jsx(hr,{style:{width:60,height:"95%",backgroundColor:Br.red,borderTopLeftRadius:2,borderTopRightRadius:2}}),me.jsx(ur,{style:Qt.barLabel,children:"High"})]'

# New DM Block with 35% height
dm_pdf_esrd_chart_corrected = 'children:[me.jsx(ur,{style:[Qt.barVal,{color:Br.red}],children:"3.5"}),me.jsx(hr,{style:{width:60,height:"35%",backgroundColor:Br.red,borderTopLeftRadius:2,borderTopRightRadius:2}}),me.jsx(ur,{style:Qt.barLabel,children:"High"})]'

non_dm_pdf_esrd_chart = 'children:[me.jsx(ur,{style:[Qt.barVal,{color:Br.red}],children:"1.6"}),me.jsx(hr,{style:{width:60,height:"16%",backgroundColor:Br.red,borderTopLeftRadius:2,borderTopRightRadius:2}}),me.jsx(ur,{style:Qt.barLabel,children:"High"})]'

# Logic: use CORRECTED DM block (35%) instead of original (95%).
repl_pdf_esrd_chart = f'children:({dm_check_pdf} ? {dm_pdf_esrd_chart_corrected[9:]} : {non_dm_pdf_esrd_chart[9:]})'


# APPLY
count = 0
if target_pdf_det in content:
    content = content.replace(target_pdf_det, repl_pdf_det)
    count += 1
else:
    # If already patched (logic exists inside), replace logic?
    # Simple replace assumes unconditional original string exists.
    # If patches were applied in v12, original strings are GONE.
    # I need to target the *Patched* string if I want to update logic.
    # Wait, v12 has the patches applied. So `target_pdf_det` (unconditional) is NOT in the file.
    # I need to find the conditional block I injected and REPLACE it with new conditional block?
    # Or start from fresh/revert? No revert available easily.
    # I can search for the conditional logic string.
    pass

# Strategy for update on already-patched file:
# Search for `children:((String(i._diabetic...` and replace the whole block.
# Since I used standard strings, I can reconstruct what the *current* state is.
# Current PDF Patch 2 (Chart 1): `... ? ...height:"95%"... : ...height:"40%"...`
# Current PDF Patch 4 (Chart 2): `... ? ...height:"95%"... : ...height:"43%"...` (Wait, I used 43%? Check previous artifacts. Yes 43%).

# I will find the incorrect patch output for Patch 4 and replace it.
# Incorrect Patch 4: `height:"95%"` (for 3.5) and `height:"43%"`? No, I check `reapply_pdf_patch.py`.
# Yes, `repl_pdf_esrd_chart` used `original` (95%) and `16%` (Wait, step 496 code: `height:"16%"`).
# Ah, Step 496: `non_dm_pdf_esrd_chart` used `16%`. 
# So Non-DM is correct (16%).
# But DM used `target_pdf_esrd_chart[9:]` which was `height:"95%"`.
# So DM is 95% (Incorrect, should be 35%).
# So I verify: I need to change DM from 95% to 35%.

# Search Pattern: 
# `? [me.jsx(ur,{style:[Qt.barVal,{color:Br.red}],children:"3.5"}),me.jsx(hr,{style:{width:60,height:"95%",backgroundColor:Br.red`
# Replace with `height:"35%"`.

current_incorrect_dm_esrd = 'children:"3.5"}),me.jsx(hr,{style:{width:60,height:"95%",backgroundColor:Br.red'
correction_dm_esrd = 'children:"3.5"}),me.jsx(hr,{style:{width:60,height:"35%",backgroundColor:Br.red'

if current_incorrect_dm_esrd in content:
    content = content.replace(current_incorrect_dm_esrd, correction_dm_esrd)
    print("Corrected DM ESRD height from 95% to 35%.")
    count += 1
else:
    print("Warning: DM ESRD 95% string not found.")

# Non-DM ESRD: I used 16% in v12. So it should be fine. 
# Step 496 code: `height:"16%"`. 
# So only DM need fix.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Patches updated: {count}")
