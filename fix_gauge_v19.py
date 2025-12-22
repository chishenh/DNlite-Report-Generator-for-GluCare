
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-17.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0

# 1. Revert HTML Width (Fm)
# Search for generic Fm definition to find current state
# `className:"flex flex-col items-center justify-end h-full`
fm_def_sig = 'className:"flex flex-col items-center justify-end h-full'
idx_fm = content.find(fm_def_sig)
if idx_fm != -1:
    # Read context to see if it is w-[60px] or w-24
    ctx = content[idx_fm:idx_fm+150]
    print(f"Fm Definition Context: {ctx}")
    if 'w-[60px]' in ctx:
        # Revert to w-24
        new_ctx = ctx.replace('w-[60px]', 'w-24')
        content = content.replace(ctx, new_ctx)
        count += 1
        print("Reverted Fm width to w-24.")
    elif 'w-24' in ctx:
        # Already reverted or never changed (maybe w-[60px] patch failed?)
        print("Fm width is already w-24. No action needed.")
    else:
        print("Fm width not recognized in context.")
else:
    print("Fm Definition not found.")

# 2. Patch b3e (Gauge)
# Replace `b3e` definition with E3e-like logic (ported to HTML)
# Original b3e start: `b3e=({value:e,threshold:t=7.53,max:r=300})=>{`
# Original b3e uniqueness: uses `g=80` (E3e used 85), `p=100` (E3e 105), `y=-180` (Logic different from E3e).
# Note: b3e uses helper `T=(ie,...`. E3e uses `N`.
# I will find the FULL b3e block and replace it.
# Start: `b3e=({value:e,threshold:t=7.53,max:r=300})=>{`
# End: `me.jsx("circle",{cx:p,cy:p,r:5,fill:V0.needle})]})}` 
# (Based on dump 693... `me.jsx("circle",{cx:p,c`... wait, I need to know the closing syntax).
# Assuming standard ending `]})}` based on structure.
# But string replacement is risky without exact match.
# I will use a known unique substring of b3e and replace the surrounding block if I can define boundaries.
# Unique string: `d:T(p,p,g,I,v),fill:"none",stroke:V0.red` (From dump 693).
# I'll search for b3e start, and then find the closing brace?
# Or I just replace the FUNCTION BODY.
# `b3e=({value:e,threshold:t=7.53,max:r=300})=>{` ...
# Replacement: `b3e=({value:e,threshold:t=7.53,max:r=300})=>{` + NEW LOGIC.
# I will define new logic first.

new_logic_body = """const n=typeof e=="number"&&!isNaN(e)?e:0,a=Math.log(1),i=Math.log(r),s=Math.max(1,Math.min(n,r)),o=Math.log(s),c=Math.log(t),f=i-a,h=(o-a)/f,d=(c-a)/f,g=85,p=105,y=140,v=77,b=-180,I=0,_=180,C=b+d*_,T=b+h*_,
k=(W,te,Z,ce)=>{const Fe=ce*Math.PI/180;return{x:W+Z*Math.cos(Fe),y:te+Z*Math.sin(Fe)}},
N=(W,te,Z,ce,Fe)=>{const ze=k(W,te,Z,Fe),_e=k(W,te,Z,ce),Se=Fe-ce<=180?"0":"1";return["M",ze.x,ze.y,"A",Z,Z,0,Se,0,_e.x,_e.y].join(" ")},
Q=65,O=5,L=T*Math.PI/180,U=y+Q*Math.cos(L),Y=p+Q*Math.sin(L),S=y+O*Math.cos(L-Math.PI/2),H=p+O*Math.sin(L-Math.PI/2),z=y+O*Math.cos(L+Math.PI/2),ie=p+O*Math.sin(L+Math.PI/2),
ee=`M ${S} ${H} L ${U} ${Y} L ${z} ${ie} Z`,re=N(y,p,g,b,C),ye=N(y,p,g,C,I),le=N(y,p,v,b,I),
V=[1,3,10,30,100,300].map(W=>{const Z=(Math.log(W)-a)/f,ce=b+Z*_,Fe=k(y,p,v,ce),ze=k(y,p,v-5,ce),_e=k(y,p,v-15,ce);return{value:W,start:Fe,end:ze,textPos:_e}});
return me.jsx("div",{style:{width:"300px",height:"160px",margin:"0 auto",position:"relative"},children:me.jsxs("svg",{width:"300",height:"160",viewBox:"0 0 280 130",xmlns:"http://www.w3.org/2000/svg",style:{overflow:"visible"},children:[
    me.jsx("path",{d:re,stroke:V0.teal,strokeWidth:16,fill:"none"}),
    me.jsx("path",{d:ye,stroke:V0.red,strokeWidth:16,fill:"none"}),
    me.jsx("path",{d:le,stroke:"black",strokeWidth:1,fill:"none"}),
    V.map((W,te)=>me.jsxs("g",{children:[
        me.jsx("line",{x1:W.start.x,y1:W.start.y,x2:W.end.x,y2:W.end.y,stroke:"black",strokeWidth:1}),
        me.jsx("text",{x:W.textPos.x,y:W.textPos.y+3,textAnchor:"middle",fontSize:"8",fill:"#64748b",children:String(W.value)})
    ]},te)),
    me.jsx("path",{d:ee,fill:V0.needle}),
    me.jsx("circle",{cx:y,cy:p,r:5,fill:V0.needle})
]})});}"""

# Now finding b3e to replace
b3e_header = 'b3e=({value:e,threshold:t=7.53,max:r=300})=>{'
idx_b3e = content.find(b3e_header)
if idx_b3e != -1:
    # We need to find the END of the function block.
    # Since we can't parse braces easily, I will search for the START of the NEXT function `Uk=` (if it follows)
    # Dump 2240852 showed `b3e`... then cut off.
    # I'll search for `const Uk` or `Uk=` or `,Uk=` that comes after.
    # Or just replace `b3e=...` until `return me.jsx("div"...` logic ends?
    # I will assumes `b3e` contains `return me.jsx("div"` and ends with `]})}`.
    # Let's string match the *old* body start.
    old_body_start = 'const n=typeof e=="number"&&!isNaN(e)?e:0,a=Math.log(1),i=Math.log(r),s=Math.max(1,Math.min(n,r)),o=Math.log(s),c=Math.log(t),f=i-a,h=(o-a)/f,d=(c-a)/f,g=80,p=100'
    idx_old = content.find(old_body_start, idx_b3e)
    
    if idx_old != -1:
        # Find the end of `me.jsx("div",...)` block.
        # Unique end string for b3e: `me.jsx("circle",{cx:p,cy:p,r:5,fill:V0.needle})]})}`
        # I'll search for this.
        # Dump 693: `me.jsx("circle",{cx:p,c`
        # Assume standard ending.
        # Search for `fill:V0.needle})]})}`
        idx_end = content.find('fill:V0.needle})]})}', idx_old)
        if idx_end != -1:
            end_pos = idx_end + len('fill:V0.needle})]})}')
            # Replace from `b3e_header` to `end_pos` (exclusive? no inclusive) with `b3e_header + new_body`.
            # Wait, `new_body` includes the header `b3e=...`?
            # My `new_logic_body` definition DOES NOT include header. it starts `const n=...`.
            # Ah, I defined `new_b3e_logic` variable above starting with `b3e=`.
            
            content = content[:idx_b3e] + new_logic_body + content[end_pos:]
            count += 1
            print("b3e (Gauge) patched with E3e logic.")
        else:
            print("Error: Could not find end of b3e function.")
            # Fallback: Try less strict end match? `fill:V0.needle})`?
    else:
        print("Error: Could not match b3e old body start.")
else:
    print("Error: b3e definition not found.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Patches updated: {count}")
