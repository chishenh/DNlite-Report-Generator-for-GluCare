
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-4.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Current styles (from previous debug output):
# cellLabelText:{fontSize:10,fontFamily:"Helvetica-Bold",color:Br.slate500}
# cellValueText:{fontSize:10,fontFamily:"Helvetica",color:Br.slate900}

# Target:
# cellLabelText:{fontSize:10,textAlign:"center",fontFamily...
# cellValueText:{fontSize:10,textAlign:"center",fontFamily...

# We can replace the substrings.
# Note: minified keys order might vary, but from dump we saw:
# cellLabelText:{fontSize:10,fontFamily:"Helvetica-Bold"
# cellValueText:{fontSize:10,fontFamily:"Helvetica"

# Replacement 1: cellLabelText
target_1 = 'cellLabelText:{fontSize:10,fontFamily:"Helvetica-Bold"'
repl_1 = 'cellLabelText:{fontSize:10,textAlign:"center",fontFamily:"Helvetica-Bold"'

# Replacement 2: cellValueText
target_2 = 'cellValueText:{fontSize:10,fontFamily:"Helvetica"'
repl_2 = 'cellValueText:{fontSize:10,textAlign:"center",fontFamily:"Helvetica"'

content_v1 = content.replace(target_1, repl_1)
content_final = content_v1.replace(target_2, repl_2)

# Verify if replacements happened
if content_v1 == content:
    print("Warning: cellLabelText replacement failed (pattern not found)")
if content_final == content_v1:
    print("Warning: cellValueText replacement failed (pattern not found)")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content_final)

print(f"Successfully added textAlign:center to {file_path}")
