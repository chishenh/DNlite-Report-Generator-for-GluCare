
import os
import re

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define markers
start_marker = 'me.jsxs(hr,{style:Qt.grid,children:['
end_marker = 'me.jsxs(hr,{style:Qt.sectionTitleWrapper,children:[me.jsx(hr,{style:Qt.sectionTitleBar}),me.jsx(ur,{style:Qt.sectionTitle,children:"DNlite Level"})'

# Locate start (after Personal Information)
# We know it's around index 2225600
# Let's find "Personal Information" first
idx_personal = content.find('children:"Personal Information"})]}),')
if idx_personal == -1:
    print("Error: Could not find Personal Information anchor")
    exit(1)

# Find start of grid
idx_grid_start = content.find(start_marker, idx_personal)
if idx_grid_start == -1:
    print("Error: Could not find grid start")
    exit(1)

# Find end marker (DNlite Level)
idx_end = content.find(end_marker, idx_grid_start)
if idx_end == -1:
    print("Error: Could not find end marker")
    exit(1)

# The text to replace is content[idx_grid_start:idx_end]
# But we need to verify where the ']})' of the grid closes.
# The end_marker starts with ',me.jsxs(' so the character before it should be ')' or ']' or '}'.
# In the dump: `children:String(i._age||"")})})]})]}),me.jsxs(hr,{style:Qt.sectionTitleWrapper`
# The grid call is `me.jsxs(hr,{style:Qt.grid,children:[ ... ]})`
# The dump shows: `i._age||"")})})]})]}),me.jsxs`
# There are brackets `]})]})` ??
# `children:[ ... ]})` matches `me.jsxs( ... )`
# So we need to cut strictly at the comma before existing end_marker.
# Let's verify character at idx_end - 1 is ','
if content[idx_end-1] != ',':
    print(f"Warning: Expected comma before end marker, found '{content[idx_end-1]}'")
    # It might be separate args?
    # Dump: `i._age||"")})})]})]}),me.jsxs`
    # The grid ends, then `]` (children of surrounding?), `})` (surrounding props?), `,` (next arg in array?)
    # "Personal Information" is inside `children:[ ... ]` of a wrapper.
    # So `grid` and `sectionTitleWrapper` are siblings in an array.
    # content[idx_grid_start] is start of `me.jsxs`
    # structure: `[ ..., GridElement, NextElement, ... ]`
    # So `content[idx_end]` should be the start of NextElement.
    # And there should be a comma before it.
    
    # We will replace from idx_grid_start up to idx_end - 1 (the comma).
    pass

# Check comma
is_comma = content[idx_end-1] == ','
replace_end = idx_end - 1 if is_comma else idx_end 
# (If no comma, maybe syntax differs, but for array elements there must be comma)

original_block = content[idx_grid_start:replace_end]
print(f"Original block length: {len(original_block)}")

# Construct new block
# Note: Using minified names 'hr', 'ur', 'Qt', 'Br', 'i'
# And matching the observed syntax exactly.

new_block = (
    'me.jsxs(hr,{style:Qt.grid,children:['
    
    # Row 1: Headers (Clinic, Sampling Date, Report Number)
    'me.jsxs(hr,{style:Qt.row,children:['
    'me.jsx(hr,{style:Qt.cellLabelContainer,children:me.jsx(ur,{style:Qt.cellLabelText,children:"Clinic"})}),'
    'me.jsx(hr,{style:Qt.cellLabelContainer,children:me.jsx(ur,{style:Qt.cellLabelText,children:"Sampling Date"})}),'
    'me.jsx(hr,{style:[Qt.cellLabelContainer,{borderRightWidth:0}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Report Number"})})'
    ']}),'
    
    # Row 2: Values (Unit, Date, ReportNo)
    'me.jsxs(hr,{style:Qt.row,children:['
    'me.jsx(hr,{style:Qt.cellValueContainer,children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._unit||"")})}),'
    'me.jsx(hr,{style:Qt.cellValueContainer,children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._date||"")})}),'
    'me.jsx(hr,{style:[Qt.cellValueContainer,{borderRightWidth:0}],children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._reportNo||"")})})'
    ']}),'

    # Row 3: Headers (Patient/MRN, Gender, Age)
    'me.jsxs(hr,{style:Qt.row,children:['
    'me.jsx(hr,{style:Qt.cellLabelContainer,children:me.jsx(ur,{style:Qt.cellLabelText,children:"Patient / MRN"})}),'
    'me.jsx(hr,{style:Qt.cellLabelContainer,children:me.jsx(ur,{style:Qt.cellLabelText,children:"Gender"})}),'
    'me.jsx(hr,{style:[Qt.cellLabelContainer,{borderRightWidth:0}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Age"})})'
    ']}),'

    # Row 4: Values (Name/MRN, Gender, Age)
    'me.jsxs(hr,{style:Qt.row,children:['
    'me.jsx(hr,{style:Qt.cellValueContainer,children:me.jsxs(ur,{style:[Qt.cellValueText,{fontFamily:"Helvetica-Bold"}],children:[String(i._name||"")," ",me.jsxs(ur,{style:{fontFamily:"Helvetica",color:Br.slate400,fontSize:9,fontWeight:"normal"},children:["/ ",String(i._mrn||"")]})]})}),'
    'me.jsx(hr,{style:Qt.cellValueContainer,children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._gender||"")})}),'
    'me.jsx(hr,{style:[Qt.cellValueContainer,{borderRightWidth:0}],children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._age||"")})})'
    ']})'

    ']})'
)

# Replace
new_content = content[:idx_grid_start] + new_block + content[replace_end:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Successfully updated layout in {file_path}")
print(f"New block length: {len(new_block)}")
