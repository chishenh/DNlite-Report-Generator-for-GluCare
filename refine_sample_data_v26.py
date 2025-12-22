
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-25.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update v (Download Template)
# Old rows from v25:
old_v_rows = (
    '["GluCare. Health","2025-12-21","1001","DM-Low Patient","MRN1001","Male","60","Dr. Wang","100","100","","Yes"],'
    '["GluCare. Health","2025-12-21","1002","DM-High Patient","MRN1002","Female","65","Dr. Wang","1000","100","","Yes"],'
    '["GluCare. Health","2025-12-21","1003","nonDM-Low Patient","MRN1003","Male","50","Dr. Wang","100","100","","No"],'
    '["GluCare. Health","2025-12-21","1004","nonDM-High Patient","MRN1004","Female","55","Dr. Wang","1000","100","","No"]'
)

new_v_rows = (
    '["GluCare. Health","2025-12-21","1001","DM-Low Patient","MRN1001","Male","60","Dr. Wang","2.5","1.0","","Yes"],'
    '["GluCare. Health","2025-12-21","1002","DM-High Patient","MRN1002","Female","65","Dr. Wang","15.0","1.0","","Yes"],'
    '["GluCare. Health","2025-12-21","1003","nonDM-Low Patient","MRN1003","Male","50","Dr. Wang","3.5","1.2","","No"],'
    '["GluCare. Health","2025-12-21","1004","nonDM-High Patient","MRN1004","Female","55","Dr. Wang","25.0","1.0","","No"]'
)

if old_v_rows in content:
    content = content.replace(old_v_rows, new_v_rows)
    print("Refined v (Download Template) successfully.")
else:
    print("Could not find old_v_rows.")

# 2. Update b (Load Sample)
old_b_body = (
    '['
    '["姓名","Age","Gender","Clinic","Sampling Date","MRN","uPTM-FetA","UCr","Diabetic"],'
    '["DM-Low Patient","60","Male","GluCare. Health","2025-12-21","1001","100","100","Yes"],'
    '["DM-High Patient","65","Female","GluCare. Health","2025-12-21","1002","1000","100","Yes"],'
    '["nonDM-Low Patient","50","Male","GluCare. Health","2025-12-21","1003","100","100","No"],'
    '["nonDM-High Patient","55","Female","GluCare. Health","2025-12-21","1004","1000","100","No"]'
    ']'
)

new_b_body = (
    '['
    '["姓名","Age","Gender","Clinic","Sampling Date","MRN","uPTM-FetA","UCr","Diabetic"],'
    '["DM-Low Patient","60","Male","GluCare. Health","2025-12-21","1001","2.5","1.0","Yes"],'
    '["DM-High Patient","65","Female","GluCare. Health","2025-12-21","1002","15.0","1.0","Yes"],'
    '["nonDM-Low Patient","50","Male","GluCare. Health","2025-12-21","1003","3.5","1.2","No"],'
    '["nonDM-High Patient","55","Female","GluCare. Health","2025-12-21","1004","25.0","1.0","No"]'
    ']'
)

if old_b_body in content:
    content = content.replace(old_b_body, new_b_body)
    print("Refined b (Load Sample) successfully.")
else:
    print("Could not find old_b_body.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
