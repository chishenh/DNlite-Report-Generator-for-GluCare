
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-29.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Target insertion point on Home Page
# Home page structure ends with Load Sample button and its containers.
# ... " Load Sample"]})]})]})]}`
# Note: The `]` is the end of the children array. We want to add BEFORE the `]`.

disclaimer_jsx = (
    ',me.jsx("div",{className:"max-w-xl text-center px-4 mt-8",children:me.jsxs("p",{className:"text-xs text-slate-400 leading-relaxed",children:['
    'me.jsx("span",{className:"font-bold block mb-1 text-slate-500",children:"免責聲明 / Disclaimer"}),'
    '"本報告產生器僅供數據輸出使用，請務必仔細檢查內容正確性。若因數據輸入錯誤或格式轉換異常導致之錯誤，本系統概不負責。",me.jsx("br",{}),'
    '"This report generator is for data output only. Please verify content accuracy carefully. We are not responsible for any errors or damages."'
    ']})})'
)

old_tail = '" Load Sample"]})]})]})'
new_tail = '" Load Sample"]})]})' + disclaimer_jsx + '})'

if old_tail in content:
    content = content.replace(old_tail, new_tail)
    print("Added disclaimer to Home Page successfully.")
else:
    print("Could not find Home Page tail signature.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
