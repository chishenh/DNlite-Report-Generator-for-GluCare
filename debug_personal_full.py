
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

idx = 2225418
start = idx
# Get enough to see all personal info fields (Clinic, Date, ReportNo, Patient, Gender, Age)
end = idx + 2000 

print(content[start:end])
