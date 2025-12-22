
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-26.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update N (Date Formatter)
old_n = 'const N=O=>typeof O=="number"&&O>2e4?new Date(Math.round((O-25569)*86400*1e3)).toISOString().split("T")[0]:O'
new_n = 'const N=O=>{if(!O)return"";let d;if(typeof O=="number"&&O>2e4)d=new Date(Math.round((O-25569)*86400*1e3));else d=new Date(O);return d instanceof Date&&!isNaN(d.getTime())?d.toISOString().split("T")[0]:O}'

if old_n in content:
    content = content.replace(old_n, new_n)
    print("Updated N successfully.")
else:
    print("Could not find old_n.")

# 2. Update Display Formatting and reportDate
# Context (from dump 1060):
# :((be===0||isNaN(be))&&le!==0&&(be=parseFloat((ye/le).toFixed(2))),U._disp_uptm=ee||ye.toString(),U._disp_dnlite=be.toFixed(2)),U._disp_ucr=re||le.toString(),U._val_dnlite=be,U._name=U[Y("姓名")]||U[Y("Name")]||"Unknown",U._age=U[Y("年齡")]||...
# ...const V=U[Y("日期")]||U[Y("Date")]||U[Y("Sampling")];return U._date=N(V)||g.date,U._reportDate=U[Y("Report Date")]||U[Y("ReportDate")]||g.date,U._inspector=...

# Target 1: Numeric display
old_disp = 'U._disp_uptm=ee||ye.toString(),U._disp_dnlite=be.toFixed(2)),U._disp_ucr=re||le.toString()'
new_disp = 'U._disp_uptm=ye.toFixed(2),U._disp_dnlite=be.toFixed(2)),U._disp_ucr=le.toFixed(2)'

if old_disp in content:
    content = content.replace(old_disp, new_disp)
    print("Updated numeric display successfully.")
else:
    print("Could not find old_disp.")

# Target 2: reportDate standardization
old_report_date = 'U._reportDate=U[Y("Report Date")]||U[Y("ReportDate")]||g.date'
new_report_date = 'U._reportDate=N(U[Y("Report Date")]||U[Y("ReportDate")])||g.date'

if old_report_date in content:
    content = content.replace(old_report_date, new_report_date)
    print("Updated reportDate successfully.")
else:
    print("Could not find old_report_date.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
