
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-28.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Target: N date formatter
old_n = 'const N=O=>{if(!O)return"";let d;if(typeof O=="number"&&O>2e4)d=new Date(Math.round((O-25569)*86400*1e3));else d=new Date(O);return d instanceof Date&&!isNaN(d.getTime())?d.toISOString().split("T")[0]:O}'

# Enhanced N to handle DD/MM/YYYY and DD-MM-YYYY
new_n = 'const N=O=>{if(!O)return"";let d;if(typeof O=="number"&&O>2e4)d=new Date(Math.round((O-25569)*86400*1e3));else if(typeof O=="string"){const m=O.match(/^(\\d{1,2})[\\/\\-](\\d{1,2})[\\/\\-](\\d{4})$/);if(m)d=new Date(`${m[3]}-${m[2]}-${m[1]}`);else d=new Date(O)}else d=new Date(O);return d instanceof Date&&!isNaN(d.getTime())?d.toISOString().split("T")[0]:O}'

if old_n in content:
    content = content.replace(old_n, new_n)
    print("Enhanced N date parsing successfully.")
else:
    print("Could not find old_n definition.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
