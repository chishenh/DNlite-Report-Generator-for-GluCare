
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-2.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Styles found:
# cellLabelContainer:{width:"20%", ...}
# cellValueContainer:{width:"30%", ...}

# Current layout we injected:
# Row 1 (Headers): Label, Label, Label
# Row 2 (Values): Value, Value, Value
# Row 3 (Headers): Label, Label, Label
# Row 4 (Values): Value, Value, Value

# Issue:
# Row 1 uses cellLabelContainer (20%) + cellLabelContainer (20%) + cellLabelContainer (20%) = 60%.
# Empty space = 40%. The "extra cell" is likely this empty space.

# Fix:
# Override styles inline for these rows.
# Width should be '33.33%'.

# We need to replace the block again.
# Locate the block we injected. It starts with 'me.jsxs(hr,{style:Qt.grid,children:['
# We can just run the same search logic as before.

start_marker = 'me.jsxs(hr,{style:Qt.grid,children:['
end_marker = 'me.jsxs(hr,{style:Qt.sectionTitleWrapper,children:[me.jsx(hr,{style:Qt.sectionTitleBar}),me.jsx(ur,{style:Qt.sectionTitle,children:"DNlite Level"})'

idx_personal = content.find('children:"Personal Information"})]}),')
idx_grid_start = content.find(start_marker, idx_personal)
idx_end = content.find(end_marker, idx_grid_start)

# Detect if comma before end marker (from previous logic)
replace_end = idx_end - 1 if content[idx_end-1] == ',' else idx_end

# Define new block with width overrides
# We'll use [Qt.cellLabelContainer, {width: "33.33%"}] syntax

new_block = (
    'me.jsxs(hr,{style:Qt.grid,children:['
    
    # Row 1: Headers (Clinic, Sampling Date, Report Number)
    'me.jsxs(hr,{style:Qt.row,children:['
    'me.jsx(hr,{style:[Qt.cellLabelContainer,{width:"33.33%"}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Clinic"})}),'
    'me.jsx(hr,{style:[Qt.cellLabelContainer,{width:"33.33%"}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Sampling Date"})}),'
    'me.jsx(hr,{style:[Qt.cellLabelContainer,{width:"33.33%",borderRightWidth:0}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Report Number"})})'
    ']}),'
    
    # Row 2: Values (Unit, Date, ReportNo)
    'me.jsxs(hr,{style:Qt.row,children:['
    'me.jsx(hr,{style:[Qt.cellValueContainer,{width:"33.33%"}],children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._unit||"")})}),'
    'me.jsx(hr,{style:[Qt.cellValueContainer,{width:"33.33%"}],children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._date||"")})}),'
    'me.jsx(hr,{style:[Qt.cellValueContainer,{width:"33.33%",borderRightWidth:0}],children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._reportNo||"")})})'
    ']}),'

    # Row 3: Headers (Patient/MRN, Gender, Age)
    'me.jsxs(hr,{style:Qt.row,children:['
    'me.jsx(hr,{style:[Qt.cellLabelContainer,{width:"33.33%"}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Patient / MRN"})}),'
    'me.jsx(hr,{style:[Qt.cellLabelContainer,{width:"33.33%"}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Gender"})}),'
    'me.jsx(hr,{style:[Qt.cellLabelContainer,{width:"33.33%",borderRightWidth:0}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Age"})})'
    ']}),'

    # Row 4: Values (Name/MRN, Gender, Age)
    'me.jsxs(hr,{style:Qt.row,children:['
    'me.jsx(hr,{style:[Qt.cellValueContainer,{width:"33.33%"}],children:me.jsxs(ur,{style:[Qt.cellValueText,{fontFamily:"Helvetica-Bold"}],children:[String(i._name||"")," ",me.jsxs(ur,{style:{fontFamily:"Helvetica",color:Br.slate400,fontSize:9,fontWeight:"normal"},children:["/ ",String(i._mrn||"")]})]})}),'
    'me.jsx(hr,{style:[Qt.cellValueContainer,{width:"33.33%"}],children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._gender||"")})}),'
    'me.jsx(hr,{style:[Qt.cellValueContainer,{width:"33.33%",borderRightWidth:0}],children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._age||"")})})'
    ']})'

    ']})'
)

new_content = content[:idx_grid_start] + new_block + content[replace_end:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Successfully fixed grid layout widths in {file_path}")
