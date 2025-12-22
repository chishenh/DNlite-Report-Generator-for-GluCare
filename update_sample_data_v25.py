
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-24.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Snippet from dump (v function):
# ["GluCare. Health","2025-12-21","1001","John Doe","MRN12345","Male","60","Dr. Wang","550","1.18","","Yes"]
old_v_row = '["GluCare. Health","2025-12-21","1001","John Doe","MRN12345","Male","60","Dr. Wang","550","1.18","","Yes"]'
new_v_rows = (
    '["GluCare. Health","2025-12-21","1001","DM-Low Patient","MRN1001","Male","60","Dr. Wang","100","100","","Yes"],'
    '["GluCare. Health","2025-12-21","1002","DM-High Patient","MRN1002","Female","65","Dr. Wang","1000","100","","Yes"],'
    '["GluCare. Health","2025-12-21","1003","nonDM-Low Patient","MRN1003","Male","50","Dr. Wang","100","100","","No"],'
    '["GluCare. Health","2025-12-21","1004","nonDM-High Patient","MRN1004","Female","55","Dr. Wang","1000","100","","No"]'
)

if old_v_row in content:
    content = content.replace(old_v_row, new_v_rows)
    print("Updated v (Download Template) successfully.")
else:
    print("Could not find old_v_row.")

# Snippets from dump (b function):
# b=()=>{p([["姓名","Age","Gender","Clinic","Sampling Date","MRN","uPTM-FetA","UCr","Diabetic"],["John Doe","60","Male","GluCare. Health","2025-10-28","16656","550","1.18","Yes"],["Jane Smith","55","Female","GluCare. Health","2025-10-28","16657","120.5","0.8","No"]])}
# Note: " 姓名" (with space) was in v17, but v24 dump showed "姓名"? 
# Wait, Step 883 dump: `b=()=>{p([["姓名","Age"`
# Let's check exactly if there's a space. 
# Step 883: `p([["姓名","Age"` -> No initial space.

old_b_body = '[["姓名","Age","Gender","Clinic","Sampling Date","MRN","uPTM-FetA","UCr","Diabetic"],["John Doe","60","Male","GluCare. Health","2025-10-28","16656","550","1.18","Yes"],["Jane Smith","55","Female","GluCare. Health","2025-10-28","16657","120.5","0.8","No"]]'
new_b_body = (
    '['
    '["姓名","Age","Gender","Clinic","Sampling Date","MRN","uPTM-FetA","UCr","Diabetic"],'
    '["DM-Low Patient","60","Male","GluCare. Health","2025-12-21","1001","100","100","Yes"],'
    '["DM-High Patient","65","Female","GluCare. Health","2025-12-21","1002","1000","100","Yes"],'
    '["nonDM-Low Patient","50","Male","GluCare. Health","2025-12-21","1003","100","100","No"],'
    '["nonDM-High Patient","55","Female","GluCare. Health","2025-12-21","1004","1000","100","No"]'
    ']'
)

if old_b_body in content:
    content = content.replace(old_b_body, new_b_body)
    print("Updated b (Load Sample) successfully.")
else:
    print("Could not find old_b_body.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
