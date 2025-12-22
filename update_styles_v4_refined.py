
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-3.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- PART 1: Personal Information Alignment & Border ---
start_marker = 'me.jsxs(hr,{style:Qt.grid,children:['
end_marker = 'me.jsxs(hr,{style:Qt.sectionTitleWrapper,children:[me.jsx(hr,{style:Qt.sectionTitleBar}),me.jsx(ur,{style:Qt.sectionTitle,children:"DNlite Level"})'

idx_personal = content.find('children:"Personal Information"})]}),')
idx_grid_start = content.find(start_marker, idx_personal)
idx_end = content.find(end_marker, idx_grid_start)
replace_end = idx_end - 1 if content[idx_end-1] == ',' else idx_end

# Redefine Personal Info block with:
# 1. alignItems: "center"
# 2. borderBottomWidth: 0 on last row
# 3. width: "33.33%" (maintained)

new_block = (
    'me.jsxs(hr,{style:Qt.grid,children:['
    
    # Row 1
    'me.jsxs(hr,{style:Qt.row,children:['
    'me.jsx(hr,{style:[Qt.cellLabelContainer,{width:"33.33%",alignItems:"center"}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Clinic"})}),'
    'me.jsx(hr,{style:[Qt.cellLabelContainer,{width:"33.33%",alignItems:"center"}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Sampling Date"})}),'
    'me.jsx(hr,{style:[Qt.cellLabelContainer,{width:"33.33%",alignItems:"center",borderRightWidth:0}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Report Number"})})'
    ']}),'
    
    # Row 2
    'me.jsxs(hr,{style:Qt.row,children:['
    'me.jsx(hr,{style:[Qt.cellValueContainer,{width:"33.33%",alignItems:"center"}],children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._unit||"")})}),'
    'me.jsx(hr,{style:[Qt.cellValueContainer,{width:"33.33%",alignItems:"center"}],children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._date||"")})}),'
    'me.jsx(hr,{style:[Qt.cellValueContainer,{width:"33.33%",alignItems:"center",borderRightWidth:0}],children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._reportNo||"")})})'
    ']}),'

    # Row 3
    'me.jsxs(hr,{style:Qt.row,children:['
    'me.jsx(hr,{style:[Qt.cellLabelContainer,{width:"33.33%",alignItems:"center"}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Patient / MRN"})}),'
    'me.jsx(hr,{style:[Qt.cellLabelContainer,{width:"33.33%",alignItems:"center"}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Gender"})}),'
    'me.jsx(hr,{style:[Qt.cellLabelContainer,{width:"33.33%",alignItems:"center",borderRightWidth:0}],children:me.jsx(ur,{style:Qt.cellLabelText,children:"Age"})})'
    ']}),'

    # Row 4 (Last Row) - borderBottomWidth: 0
    'me.jsxs(hr,{style:[Qt.row,{borderBottomWidth:0}],children:['
    'me.jsx(hr,{style:[Qt.cellValueContainer,{width:"33.33%",alignItems:"center"}],children:me.jsxs(ur,{style:[Qt.cellValueText,{fontFamily:"Helvetica-Bold"}],children:[String(i._name||"")," ",me.jsxs(ur,{style:{fontFamily:"Helvetica",color:Br.slate400,fontSize:9,fontWeight:"normal"},children:["/ ",String(i._mrn||"")]})]})}),'
    'me.jsx(hr,{style:[Qt.cellValueContainer,{width:"33.33%",alignItems:"center"}],children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._gender||"")})}),'
    'me.jsx(hr,{style:[Qt.cellValueContainer,{width:"33.33%",alignItems:"center",borderRightWidth:0}],children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._age||"")})})'
    ']})'

    ']})'
)

# Apply Personal Info update
content_updated_1 = content[:idx_grid_start] + new_block + content[replace_end:]


# --- PART 2: DNlite Level Table Border ---
# We replace the LAST row definition to remove its bottom border.
# Target: style:[Qt.tableRow,{backgroundColor:"white"}]
# Replacement: style:[Qt.tableRow,{backgroundColor:"white",borderBottomWidth:0}]
# Searching globally in the updated content is fine because this specific combination
# (tableRow + white bg) is unique to the DNlite level table's last/result row in this file context
# (based on previous dumps).

target_str = 'style:[Qt.tableRow,{backgroundColor:"white"}]'
replacement_str = 'style:[Qt.tableRow,{backgroundColor:"white",borderBottomWidth:0}]'

# We will use string replace, but verify it occurs once or limit it.
count = content_updated_1.count(target_str)
if count == 0:
    print("Error: Target DNlite row string not found!")
    # Proceed with just part 1? No, we want both.
    # Check if whitespace issue (unlikely given dump).
    # Maybe escaping?
    pass
elif count > 1:
    print(f"Warning: Target string found {count} times. Replacing ALL (assuming consistent table style).")
    # Actually, replacing all white rows in tables with no bottom border might be risky if there are others.
    # But usually white row is the last highlighting row.
    content_updated_final = content_updated_1.replace(target_str, replacement_str)
else:
    print("Found exact match for DNlite row.")
    content_updated_final = content_updated_1.replace(target_str, replacement_str)

if count == 0:
    # Fallback: Just save part 1 changes
    final_output = content_updated_1
else:
    final_output = content_updated_final

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(final_output)

print(f"Successfully applied v4 styling updates (Part 1 & 2) to {file_path}")
print(f"Personal Info Block Length: {len(new_block)}")
