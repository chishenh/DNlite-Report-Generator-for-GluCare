
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-17.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0

# 1. Revert HTML Width
target_width = 'className:"flex flex-col items-center justify-end h-full w-[60px] mx-3 group"'
repl_width = 'className:"flex flex-col items-center justify-end h-full w-24 mx-3 group"'
if target_width in content:
    content = content.replace(target_width, repl_width)
    count += 1
    print("HTML Width reverted to w-24.")
else:
    print("Error: HTML Width w-[60px] target not found.")

# 2. Define GaugeHtml Component
# Ported from E3e. Swapping logic to use HTML tags and V0 colors.
# Note: E3e uses `me.jsxs` (React). HTML also uses `me.jsxs`.
# We need to ensure `V0` is available. `Fm` uses `V0`.
# We need to map `Br` colors to `V0`.
# E3e: `Br.teal`, `Br.red`, `Br.needle`.
# Fm: `V0.teal`, `V0.red`.
# `Br.needle` probably not on V0. Assume "black" or V0.slate700?
# E3e dump showed: `me.jsx(Gd,{d:le,stroke:"black",strokeWidth:1,fill:"none"})` -> Inner line.
# `me.jsx(Gd,{d:ee,fill:Br.needle})` -> Needle.
# I'll use "black" for needle/stroke if V0 doesn't have it.

# Logic for Gauge:
# We need to inject the function definition `const GaugeHtml = ...`.
# Best place: Before the component that renders the HTML report.
# Search for `function Fm` and place it after.
idx_fm = content.find('function Fm')
if idx_fm == -1:
    idx_fm = content.find('const Fm=')

# E3e Logic (Ported)
# Using `div` and `svg`.
# Replace `k`, `N` helpers? They are defined INSIDE E3e in the dump.
# So I should copy the whole body.
gauge_code = """
const GaugeHtml=({value:e,threshold:t=7.53,max:r=300})=>{
  const n=typeof e=="number"&&!isNaN(e)?e:0,a=Math.log(1),i=Math.log(r),s=Math.max(1,Math.min(n,r)),o=Math.log(s),c=Math.log(t),f=i-a,h=(o-a)/f,d=(c-a)/f,g=85,p=105,y=140,v=77,b=-180,I=0,_=180,C=b+d*_,T=b+h*_,
  k=(W,te,Z,ce)=>{const Fe=ce*Math.PI/180;return{x:W+Z*Math.cos(Fe),y:te+Z*Math.sin(Fe)}},
  N=(W,te,Z,ce,Fe)=>{const ze=k(W,te,Z,Fe),_e=k(W,te,Z,ce),Se=Fe-ce<=180?"0":"1";return["M",ze.x,ze.y,"A",Z,Z,0,Se,0,_e.x,_e.y].join(" ")},
  Q=65,O=5,L=T*Math.PI/180,U=y+Q*Math.cos(L),Y=p+Q*Math.sin(L),S=y+O*Math.cos(L-Math.PI/2),H=p+O*Math.sin(L-Math.PI/2),z=y+O*Math.cos(L+Math.PI/2),ie=p+O*Math.sin(L+Math.PI/2),
  ee=`M ${S} ${H} L ${U} ${Y} L ${z} ${ie} Z`,re=N(y,p,g,b,C),ye=N(y,p,g,C,I),le=N(y,p,v,b,I),
  V=[1,3,10,30,100,300].map(W=>{const Z=(Math.log(W)-a)/f,ce=b+Z*_,Fe=k(y,p,v,ce),ze=k(y,p,v-5,ce),_e=k(y,p,v-15,ce);return{value:W,start:Fe,end:ze,textPos:_e}});
  return me.jsxs("svg",{width:"280",height:"130",viewBox:"0 0 280 130",children:[
    me.jsx("path",{d:re,stroke:V0.teal,strokeWidth:16,fill:"none"}),
    me.jsx("path",{d:ye,stroke:V0.red,strokeWidth:16,fill:"none"}),
    me.jsx("path",{d:le,stroke:"black",strokeWidth:1,fill:"none"}),
    V.map((W,te)=>me.jsxs("g",{children:[
        me.jsx("line",{x1:W.start.x,y1:W.start.y,x2:W.end.x,y2:W.end.y,stroke:"black",strokeWidth:1}),
        me.jsx("text",{x:W.textPos.x,y:W.textPos.y+3,textAnchor:"middle",fontSize:"8",fill:"#475569",children:String(W.value)})
    ]},te)),
    me.jsx("path",{d:ee,fill:"#334155"}),
    me.jsx("circle",{cx:y,cy:p,r:5,fill:"#334155"})
  ]})
};
"""
# Note: Replaced `Vf`->`svg`, `Gd`->`path`, `Sb`->`line`, `ur`->`text`, `Db`->`circle`.
# Replaced `Br.teal`->`V0.teal`, `Br.red`->`V0.red`, `Br.needle`->`#334155` (Slate-700).
# Replaced `Br.slate600`->`#475569` (Slate-600).
# Wrapped V loop in `g`.
# This defines `GaugeHtml` in global scope (or variable scope).

# Inject Definition
if idx_fm != -1:
    content = content[:idx_fm] + gauge_code + content[idx_fm:]
    count += 1
    print("GaugeHtml Definition Injected.")
else:
    print("Error: Location to inject GaugeHtml definition not found.")


# 3. Inject Component Usage
# Target: HTML DNlite Table.
# Search `children:"DNlite (uPTM-FetA/UCr)"` -> `</tbody></table>`.
# Insert `<div className="flex justify-center mt-4"><GaugeHtml value={parseFloat(C._val_dnlite||0)} /></div>`
# I'll target the closing `</table>` of the DNlite table.
# There might be multiple tables. I need the one with "DNlite" header.
# Strategy: Find "DNlite (uPTM-FetA/UCr)", then find next `</table>`.

idx_header = content.find('children:"DNlite (uPTM-FetA/UCr)"')
if idx_header != -1:
    idx_end_table = content.find('</table>', idx_header)
    if idx_end_table != -1:
        # Check context
        print(f"Injecting Gauge at {idx_end_table}")
        # Insert AFTER table.
        # Logic: `</table>` is string.
        # `me.jsxs("table"...` returns the table.
        # Need to know if "table" is child of a `div`.
        # Previous dump 2253257: `me.jsx("div",{className:"overflow-x-auto",children:me.jsxs("table",...`
        # So I should inject AFTER `</table>`.
        # `</table>` closes the JSX tag? No, `</table>` string is in `me.jsxs("table"...` equivalent?
        # NO! JS bundle uses `me.jsx("table",...)`. It does NOT contain `</table>` string literals usually.
        # It uses function calls.
        # I need to find the CLOSING PAREN of `me.jsxs("table",...)`.
        # This is hard to match with string replace.
        # Alternatives:
        # Match `me.jsx(Fm`? No, that's in Definition of Risk.
        # Match the header string and traverse?
        # Match the `tbody` end?
        # The dump shows `me.jsxs("tbody",{children:[...` then `]})` then `]})` (end table) then `})` (end div)?
        # I'll rely on the structure:
        # `children:"DNlite (uPTM-FetA/UCr)"` ... `children:"Cut-off: 7.53"` (from dump 2230099 for PDF... wait 2230099 was PDF! I need HTML!)
        # Re-check Dump 2253257 (HTML).
        # `children:"DNlite (uPTM-FetA/UCr)"` ... `children:i._val_unit||""` or similar.
        # How does the HTML table end?
        # `me.jsxs("tbody",...` `tr`... `] }) ] })` (table, then div).
        # I want to inject Gauge AFTER the table div.
        # I will replace `children:[me.jsxs("table",` with `children:[me.jsxs("table",` ? No.
        # I'll search for the *Heading* "DNlite Level" (HTML) and the valid container.
        # Dump 2253257:
        # `me.jsx("h3",{className:"text-base font-bold text-slate-800 mb-3 border-l-4 border-slate-800 pl-3",children:"DNlite Level"}),me.jsx("div",{className:"overflow-x-auto",children:me.jsxs("table",...`
        # The container has `children:[Heading, TableDiv]`.
        # I want `children:[Heading, TableDiv, GaugeDiv]`.
        # So I will target `children:"DNlite Level"` and `TableDiv`.
        # And Append GaugeDiv.
        
        target_dnlite_sect = 'children:"DNlite Level"}),me.jsx("div",{className:"overflow-x-auto",children:me.jsxs("table"'
        # This string identifies the start.
        # I can try to replace the *start* of the Next section?
        # Next section is "Definition of Risk".
        # `children:"Renal Function Deterioration"`
        # So `DNlite Level` section ends before `Renal Function Deterioration`.
        # I can insert Gauge BEFORE `Renal Function Deterioration` block.
        # Target: `me.jsx("h3",{className:"text-base font-bold text-slate-800 mb-3 border-l-4 border-slate-800 pl-3",children:"Renal Function Deterioration"})`
        # Insert Gauge BEFORE this.
        
        target_next_sect = 'me.jsx("h3",{className:"text-base font-bold text-slate-800 mb-3 border-l-4 border-slate-800 pl-3",children:"Renal Function Deterioration"})'
        gauge_markup = 'me.jsx("div",{className:"flex justify-center mt-6 mb-6",children:me.jsx(GaugeHtml,{value:parseFloat(C._val_dnlite||0)})}),'
        
        if target_next_sect in content:
            content = content.replace(target_next_sect, gauge_markup + target_next_sect)
            count += 1
            print("Gauge Component Injected.")
        else:
            print("Error: Target 'Renal Function Deterioration' not found for injection.")
else:
    print("Error: Header not found (logic check failed).")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Patches updated: {count}")
