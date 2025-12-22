
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-9.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Hardcoded sample data starts with `b=()=>{p([["姓名` or `b=()=>{p([`
# Previous dump: `b=()=>{p([["姓名","Age","Gender","Clinic","Sampling Date","MRN","uPTM-FetA","UCr"],["John Doe","60","Male","GluCare. Health","2025-10-28","16656","550","1.18"],["Jane Smith","55","Female","GluCare. Health","2025-10-28","16657","120.5","0.8"]])},I=`

target_data = 'b=()=>{p([["姓名","Age","Gender","Clinic","Sampling Date","MRN","uPTM-FetA","UCr"],["John Doe","60","Male","GluCare. Health","2025-10-28","16656","550","1.18"],["Jane Smith","55","Female","GluCare. Health","2025-10-28","16657","120.5","0.8"]])}'

# Modify to include "Diabetic" column and data
# Row 1 (Header): Add "Diabetic"
# Row 2 (John Doe): Add "Yes" (DM)
# Row 3 (Jane Smith): Add "No" (Non-DM) -- We can check her report to verify Non-DM logic

repl_data = 'b=()=>{p([["姓名","Age","Gender","Clinic","Sampling Date","MRN","uPTM-FetA","UCr","Diabetic"],["John Doe","60","Male","GluCare. Health","2025-10-28","16656","550","1.18","Yes"],["Jane Smith","55","Female","GluCare. Health","2025-10-28","16657","120.5","0.8","No"]])}'

if target_data in content:
    content = content.replace(target_data, repl_data)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Sample data updated to include Diabetic column.")
else:
    print("Error: Sample data target not found.")
