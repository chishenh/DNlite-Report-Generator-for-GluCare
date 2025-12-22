
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-3.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- PART 1: Personal Information Alignment & Border ---
# We previously injected this block.
# We need to find it again and replace it with the centered version + last row border fix.

start_marker_personal = 'me.jsxs(hr,{style:Qt.grid,children:['
end_marker_personal = 'me.jsxs(hr,{style:Qt.sectionTitleWrapper,children:[me.jsx(hr,{style:Qt.sectionTitleBar}),me.jsx(ur,{style:Qt.sectionTitle,children:"DNlite Level"})'

idx_personal = content.find('children:"Personal Information"})]}),')
idx_grid_start = content.find(start_marker_personal, idx_personal)
idx_end_personal = content.find(end_marker_personal, idx_grid_start)
replace_end_personal = idx_end_personal - 1 if content[idx_end_personal-1] == ',' else idx_end_personal

# Build new block with:
# 1. alignItems: "center" in all cellLabelContainer and cellValueContainer styles (inline override)
# 2. borderBottomWidth: 0 in the LAST me.jsxs(hr,{style:Qt.row ...})
# Previous fix assumed 33.33% widths. We keep that.

personal_block = (
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

    # Row 4 (Last Row) - Added borderBottomWidth: 0
    'me.jsxs(hr,{style:[Qt.row,{borderBottomWidth:0}],children:['
    'me.jsx(hr,{style:[Qt.cellValueContainer,{width:"33.33%",alignItems:"center"}],children:me.jsxs(ur,{style:[Qt.cellValueText,{fontFamily:"Helvetica-Bold"}],children:[String(i._name||"")," ",me.jsxs(ur,{style:{fontFamily:"Helvetica",color:Br.slate400,fontSize:9,fontWeight:"normal"},children:["/ ",String(i._mrn||"")]})]})}),'
    'me.jsx(hr,{style:[Qt.cellValueContainer,{width:"33.33%",alignItems:"center"}],children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._gender||"")})}),'
    'me.jsx(hr,{style:[Qt.cellValueContainer,{width:"33.33%",alignItems:"center",borderRightWidth:0}],children:me.jsx(ur,{style:Qt.cellValueText,children:String(i._age||"")})})'
    ']})'

    ']})'
)

# Apply personal change to content variable
# Note: We must be careful not to use old content index if we do multiple replacements.
# But since we read the file once, we can just split and join.
# However, DNlite table is FURTHER down in the file (after Personal Info).
# So we can apply Personal Info patch, then search for DNlite table in the NEW content (or use offset logic).

# Let's verify DNlite table comes AFTER. Yes it does.
# So:
content_intermediate = content[:idx_grid_start] + personal_block + content[replace_end_personal:]


# --- PART 2: DNlite Level Table Border ---
# Search for the LAST row of DNlite table.
# Start marker: 'children:"DNlite Level"})]}),'
# Then find 'Qt.table'.
# Inside table, there are rows.
# Last row identifier: contains "Cut-off: 7.53" or "DNlite (uPTM-FetA/UCr)"
# From dump:
# me.jsxs(hr,{style:[Qt.tableRow,{backgroundColor:"white"}],children:[ ... "Cut-off: 7.53" ... ]})
# This is the last row.
# We want to change `style:[Qt.tableRow,{backgroundColor:"white"}]` 
# to `style:[Qt.tableRow,{backgroundColor:"white",borderBottomWidth:0}]`

# Let's find that string in content_intermediate.
target_row_str = 'style:[Qt.tableRow,{backgroundColor:"white"}]'
idx_target = content_intermediate.find(target_row_str)

if idx_target != -1:
    print("Found DNlite table last row.")
    replacement_row_str = 'style:[Qt.tableRow,{backgroundColor:"white",borderBottomWidth:0}]'
    final_content = content_intermediate.replace(target_row_str, replacement_row_str, 1) # Only replace first occurrence (should be unique enough or at least correct context if we search from known point)
    # Actually, verify uniqueness or searching from correct offset.
    # The string seems unique enough for this file context, but safer to limit scope.
    # But content.replace() is global if not careful.
    # Using count=1 is safer if we are sure it's the right one.
    # It's likely the only white background row? No, others might be.
    # Let's search specifically after "DNlite Level".
    
    idx_dnlite_start = final_content.find('children:"DNlite Level"})]}),')
    if idx_dnlite_start != -1:
        # Find the target string AFTER this point
        idx_real_target = final_content.find(target_row_str, idx_dnlite_start)
        if idx_real_target != -1:
             final_content = final_content[:idx_real_target] + replacement_row_str + final_content[idx_real_target + len(target_row_str):]
        else:
             print("Warning: Could not find target row after DNlite start")
    else:
        print("Warning: Could not find DNlite start in intermediate content")

else:
    print("Error: Could not find DNlite table last row string")
    final_content = content_intermediate


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(final_content)

print(f"Successfully applied v4 styling updates to {file_path}")
