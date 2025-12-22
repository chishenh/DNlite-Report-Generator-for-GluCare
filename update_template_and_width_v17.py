
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-16.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0

# 1. Update Template Headers
# Target: `const T=[["Clinic","Sampling Date","Report Number","Patient Name","MRN","Gender","Age","Lab. Director","uPTM-FetA","Urine creatinine (UCr)","DNlite (uPTM-FetA/UCr)"]`
# Replace with: `... "DNlite (uPTM-FetA/UCr)","Diabetic"]`
# And Data Row: `["GluCare. Health","2025-12-21","1001","John Doe","MRN12345","Male","60","Dr. Wang","550","1.18",""]`
# Replace with: `... "1.18","","Yes"]`

target_headers = '["Clinic","Sampling Date","Report Number","Patient Name","MRN","Gender","Age","Lab. Director","uPTM-FetA","Urine creatinine (UCr)","DNlite (uPTM-FetA/UCr)"]'
repl_headers = '["Clinic","Sampling Date","Report Number","Patient Name","MRN","Gender","Age","Lab. Director","uPTM-FetA","Urine creatinine (UCr)","DNlite (uPTM-FetA/UCr)","Diabetic"]'

target_data = '["GluCare. Health","2025-12-21","1001","John Doe","MRN12345","Male","60","Dr. Wang","550","1.18",""]'
repl_data = '["GluCare. Health","2025-12-21","1001","John Doe","MRN12345","Male","60","Dr. Wang","550","1.18","","Yes"]'

if target_headers in content:
    content = content.replace(target_headers, repl_headers)
    count += 1
    print("Template Headers Updated.")
else:
    print("Error: Template Headers target not found.")

if target_data in content:
    content = content.replace(target_data, repl_data)
    count += 1
    print("Template Data Row Updated.")
else:
    print("Error: Template Data Row target not found.")


# 2. Revert PDF Chart Width 96 -> 60
target_pdf_width = 'style:{width:96,height:'
repl_pdf_width = 'style:{width:60,height:'

if target_pdf_width in content:
    c_pdf = content.count(target_pdf_width)
    content = content.replace(target_pdf_width, repl_pdf_width)
    count += c_pdf
    print(f"PDF Chart Width reverted to 60 ({c_pdf} occurrences).")
else:
    print("Error: PDF Width 96 target not found.")


# 3. Update HTML Chart Width `w-24` -> `w-[60px]`
# Target: `className:"flex flex-col items-center justify-end h-full w-24 mx-3 group"`
# Replace `w-24` with `w-[60px]`.
target_html_width = 'className:"flex flex-col items-center justify-end h-full w-24 mx-3 group"'
repl_html_width = 'className:"flex flex-col items-center justify-end h-full w-[60px] mx-3 group"'

if target_html_width in content:
    content = content.replace(target_html_width, repl_html_width)
    count += 1
    print("HTML Chart Width updated to 60px.")
else:
    print("Error: HTML Width target not found.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Patches updated: {count}")
