
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-30.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

home_start = 'e===1?me.jsxs("div",{className:"min-h-screen bg-slate-50 flex flex-col items-center justify-center p-6 space-y-8",children:['
home_end_marker = ':me.jsxs("div",{className:"min-h-screen bg-slate-200'

disclaimer_code = (
    'me.jsx("div",{className:"max-w-xl text-center px-4 mt-8",children:me.jsxs("p",{className:"text-xs text-slate-400 leading-relaxed",children:['
    'me.jsx("span",{className:"font-bold block mb-1 text-slate-500",children:"免責聲明 / Disclaimer"}),'
    '"本報告產生器僅供數據輸出使用，請務必仔細檢查內容正確性。若因數據輸入錯誤或格式轉換異常導致之錯誤，本系統概不負責。",me.jsx("br",{}),'
    '"This report generator is for data output only. Please verify content accuracy carefully. We are not responsible for any errors or damages."'
    ']})})'
)

new_home_block = (
    'e===1?me.jsxs("div",{className:"min-h-screen bg-slate-50 flex flex-col items-center justify-center p-6 space-y-8",children:['
    'me.jsxs("div",{className:"text-center",children:[me.jsxs("h1",{className:"text-4xl font-extrabold text-slate-800",children:["DNlite Report ",me.jsx("span",{style:{color:V0.teal},children:"for GluCare"})]}),me.jsx("p",{className:"text-slate-500 mt-2",children:"Vector PDF Engine"})]}),'
    'me.jsxs("div",{className:"bg-white p-10 rounded-2xl shadow-sm border-2 border-dashed border-slate-300 flex flex-col items-center transition-all",children:[me.jsxs("label",{className:"cursor-pointer text-white px-8 py-3 rounded-xl font-bold shadow-lg transition transform active:scale-95",style:{backgroundColor:V0.teal},children:["Upload Excel File",me.jsx("input",{type:"file",accept:".xlsx, .csv",className:"hidden",onChange:y})]}),me.jsxs("div",{className:"flex gap-4 mt-6",children:[me.jsxs("button",{onClick:v,className:"text-sm font-medium text-slate-500 hover:text-teal-600 flex items-center gap-2 px-4 py-2 bg-slate-50 rounded-lg hover:bg-slate-100 transition",children:[me.jsx(M8,{className:"w-4 h-4"})," Download Template"]}),me.jsxs("button",{onClick:b,className:"text-sm font-medium text-slate-500 hover:text-teal-600 flex items-center gap-2 px-4 py-2 bg-slate-50 rounded-lg hover:bg-slate-100 transition",children:[me.jsx(bU,{className:"w-4 h-4"})," Load Sample"]})]})]}),'
    + disclaimer_code + ']})'
)

start_idx = content.find(home_start)
if start_idx != -1:
    end_idx = content.find(home_end_marker, start_idx)
    if end_idx != -1:
        prefix = content[:start_idx]
        suffix = content[end_idx:]
        content = prefix + new_home_block + suffix
        # One last safety check: count open and close braces
        # We need to make sure the braces are balanced within the replacement.
        print("Replaced home page block successfully.")
    else:
        print("Could not find end marker.")
else:
    print("Could not find start marker.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
