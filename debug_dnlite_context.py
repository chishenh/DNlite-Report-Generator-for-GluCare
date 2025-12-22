
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-3.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Apply Personal Info patch first (simulation)
start_marker_personal = 'me.jsxs(hr,{style:Qt.grid,children:['
end_marker_personal = 'me.jsxs(hr,{style:Qt.sectionTitleWrapper,children:[me.jsx(hr,{style:Qt.sectionTitleBar}),me.jsx(ur,{style:Qt.sectionTitle,children:"DNlite Level"})'

idx_personal = content.find('children:"Personal Information"})]}),')
idx_grid_start = content.find(start_marker_personal, idx_personal)
idx_end_personal = content.find(end_marker_personal, idx_grid_start)
replace_end_personal = idx_end_personal - 1 if content[idx_end_personal-1] == ',' else idx_end_personal

# Just look at what immediately follows the Personal Info block (which we know ends at replace_end_personal)
# We expect DNlite Level logic to be there.

print("--- DNlite Level Context ---")
start_context = replace_end_personal
end_context = start_context + 2000
print(content[start_context:end_context])
