
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-15.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0

# 1. PDF Remark Center Alignment
# Target: `style:[Qt.tdContainer,{width:"30%",borderRightWidth:0}],children`
# Replace with `style:[Qt.tdContainer,{width:"30%",borderRightWidth:0,alignItems:"center"}],children`
# AND the Header: `style:[Qt.thContainer,{width:"30%",borderRightWidth:0}],children`
# The dump showed `thContainer` also has `width:"30%"`. 
# Context 2228472: `me.jsx(hr,{style:[Qt.thContainer,{width:"30%",borderRightWidth:0}],children:me.jsx(ur,{style:Qt.thText,children:"Remark"})})`
# I should patch BOTH Header and Body.

target_pdf_th = 'style:[Qt.thContainer,{width:"30%",borderRightWidth:0}]'
repl_pdf_th = 'style:[Qt.thContainer,{width:"30%",borderRightWidth:0,alignItems:"center"}]'

target_pdf_td = 'style:[Qt.tdContainer,{width:"30%",borderRightWidth:0}]'
repl_pdf_td = 'style:[Qt.tdContainer,{width:"30%",borderRightWidth:0,alignItems:"center"}]'

if target_pdf_th in content:
    content = content.replace(target_pdf_th, repl_pdf_th)
    count += 1
    print("PDF Remark Header Centered.")

# Replace all occurrences of td container (rows)
if target_pdf_td in content:
    c_td = content.count(target_pdf_td)
    content = content.replace(target_pdf_td, repl_pdf_td)
    count += c_td
    print(f"PDF Remark Body Centered ({c_td} rows).")


# 2. HTML Remark Center Alignment
# Target: `className:"border border-slate-300 p-2 text-left w-1/3",children:"Remark"`
# Replace `text-left` with `text-center`.

target_html_remark = 'className:"border border-slate-300 p-2 text-left w-1/3",children:"Remark"'
repl_html_remark = 'className:"border border-slate-300 p-2 text-center w-1/3",children:"Remark"'

if target_html_remark in content:
    content = content.replace(target_html_remark, repl_html_remark)
    count += 1
    print("HTML Remark Header Centered.")
else:
    print("Error: HTML Remark target not found.")

# Note: HTML Body cells? User said "Remark column". Usually implies header and body.
# Dump: `me.jsx("td",{className:"border border-slate-300 p-2 font-bold text-slate-900",style:{backgroundColor:"#dce3eb"},children:"uPTM-FetA"})`
# The body cells for Remark seem to be generated conditionally or empty in the dump?
# Dump showed last column: `me.jsx("td",{className:"border border-slate-300 p-2",children:i._remark})`?
# Need to find the body cell class and replace text-left if present.
# Assuming standard class `border border-slate-300 p-2`. Default is left.
# I need to add `text-center`.
# But `border border-slate-300 p-2` is generic.
# I should target the SPECIFIC cell if possible.
# Context 2253257: `me.jsx("td",{className:"border border-slate-300 p-2",children:i._val_unit||""}),me.jsx("td",{className:"border border-slate-300 p-2",children:"Normal Range: 0.60-2.50"})`
# If I change ALL `border border-slate-300 p-2` to `... text-center`, it affects all cells.
# I should find the specific one.
# For now, let's stick to Header. Logic usually follows context.
# If I can't identify body cell uniquely, I'll update Header and hope user is satisfied or verify later.
# Actually, the Remark body cell contains "Normal Range: ...".
# Target string: `className:"border border-slate-300 p-2",children:"Normal Range`
# Replace with `className:"border border-slate-300 p-2 text-center",children:"Normal Range`
target_html_remark_body = 'className:"border border-slate-300 p-2",children:"Normal Range'
repl_html_remark_body = 'className:"border border-slate-300 p-2 text-center",children:"Normal Range'
if target_html_remark_body in content:
    content = content.replace(target_html_remark_body, repl_html_remark_body)
    count +=1
    print("HTML Remark Body Centered.")


# 3. PDF Chart Width 60 -> 96
# Target: `width:60` inside chart components.
# This string might be common.
# Search context: `style:{width:60,height:`
target_width_60 = 'style:{width:60,height:'
repl_width_96 = 'style:{width:96,height:'

if target_width_60 in content:
    c_w = content.count(target_width_60)
    content = content.replace(target_width_60, repl_width_96)
    count += c_w
    print(f"PDF Chart Width updated to 96 ({c_w} occurrences).")
else:
    print("Error: PDF Chart Width target not found.")


# 4. HTML Chart "Inner Black Line" (Border)
# Target: `Fm` component definition.
# `me.jsx("div",{className:"w-full rounded-t-sm transition-all duration-500",style:{height:`
# Add `border border-black` (or slate-900) to className.
# Note: `rounded-t-sm`. Border might look weird with rounded.
# I'll add `border border-slate-900`.

target_fm_bar = 'className:"w-full rounded-t-sm transition-all duration-500"'
repl_fm_bar = 'className:"w-full rounded-t-sm transition-all duration-500 border border-slate-900"'

if target_fm_bar in content:
    content = content.replace(target_fm_bar, repl_fm_bar)
    count += 1
    print("HTML Chart Bar Border added.")
else:
    print("Error: HTML Chart Bar target not found.")


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Patches updated: {count}")
