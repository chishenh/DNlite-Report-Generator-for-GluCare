
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-21.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Nesting in E3e
# Found in v21: `E3e=(...)=>{b3e=(...)=>{...`
bad_header = 'E3e=({value:e,threshold:t=7.53,max:r=300})=>{b3e=({value:e,threshold:t=7.53,max:r=300})=>{'
good_header = 'E3e=({value:e,threshold:t=7.53,max:r=300})=>{'

if bad_header in content:
    content = content.replace(bad_header, good_header, 1)
    print("Fixed E3e/b3e nesting.")
    
    # We also need to remove the extra closing brace/paren I added in v21/v20
    # In v21 I did: `});},Fm=` fallback.
    # In v20 Context 746: `...needle})]})});})},Fm=`
    # If I removed the nested definition, I need to see what's left.
    # E3e body was replaced by b3e body.
    # E3e used to end with `]})}`.
    # My patch ended with `]})});}`. (Plus the phantom brace I removed in v21).
    # Let's search for E3e end area.
    # It's before `Uk=`.
    # Dump 778 showed: `...needle})]})},Uk=`
    # Wait, 778 dump for the NESTED block showed it ended with `]})},Uk=`.
    # This implies the nested `b3e` body (which I injected into E3e) already matches E3e ending?
    # Yes, E3e and b3e (original) were very similar.
    # So removing the header `b3e=...=>{` should fix E3e.
else:
    print("Bad nesting header not found.")

# 2. Restore b3e (HTML Gauge) at its own location
# I need to find where b3e WAS and put it back.
# Or just find the BROKEN b3e (if it's still somewhere else).
# The dump 778 only showed one b3e definition (the nested one).
# This means the original b3e was probably overwritten.
# I will search for jsx(b3e, and put a definition before it? 
# No, messy.
# I'll search for `Fm=` and put `b3e` before it.
# Fm definition in v21 is at 2242637.
# I'll prepend b3e logic there.

original_b3e = """b3e=({value:e,threshold:t=7.53,max:r=300})=>{const n=typeof e=="number"&&!isNaN(e)?e:0,a=Math.log(1),i=Math.log(r),s=Math.max(1,Math.min(n,r)),o=Math.log(s),c=Math.log(t),f=i-a,h=(o-a)/f,d=(c-a)/f,g=80,p=100,y=-180,v=0,b=180,I=y+d*b,_=y+h*b,C=(ie,ee,re,ye)=>{const le=ye*Math.PI/180;return{x:ie+re*Math.cos(le),y:ee+re*Math.sin(le)}},T=(ie,ee,re,ye,le)=>{const be=C(ie,ee,re,le),V=C(ie,ee,re,ye),W=le-ye<=180?"0":"1";return["M",be.x,be.y,"A",re,re,0,W,0,V.x,V.y].join(" ")},k=g-8,N=6,Q=_*Math.PI/180,O=p+k*Math.cos(Q),L=p+k*Math.sin(Q),U=p+N*Math.cos(Q-Math.PI/2),Y=p+N*Math.sin(Q-Math.PI/2),S=p+N*Math.cos(Q+Math.PI/2),H=p+N*Math.sin(Q+Math.PI/2),z=`M ${U} ${Y} L ${O} ${L} L ${S} ${H} Z`;return me.jsx("div",{style:{width:"300px",height:"160px",margin:"0 auto",position:"relative"},children:me.jsxs("svg",{width:"300",height:"160",viewBox:"0 0 200 110",xmlns:"http://www.w3.org/2000/svg",style:{overflow:"visible"},children:[me.jsx("path",{d:T(p,p,g,y,I),fill:"none",stroke:V0.teal,strokeWidth:"16"}),me.jsx("path",{d:T(p,p,g,I,v),fill:"none",stroke:V0.red,strokeWidth:"16"}),me.jsx("text",{x:C(p,p,g+20,I).x,y:C(p,p,g+20,I).y,textAnchor:"middle",fontSize:"10",fill:"#64748b",fontWeight:"bold",children:t}),me.jsx("text",{x:C(p,p,g+20,y).x,y:C(p,p,g+20,y).y+5,textAnchor:"start",fontSize:"10",fill:"#94a3b8",children:"1"}),me.jsx("text",{x:C(p,p,g+20,v).x,y:C(p,p,g+20,v).y+5,textAnchor:"end",fontSize:"10",fill:"#94a3b8",children:"300"}),me.jsx("path",{d:z,fill:V0.needle}),me.jsx("circle",{cx:p,cy:p,r:5,fill:V0.needle})]})})},"""

# Note: The original b3e dump (693) ended with `me.jsx("circle",{cx:p,c`
# I reconstructed the tail based on the div/svg pattern.
# Re-checking dump 693: `... needle})})}`. Yes.
# I added `,` at the end to fit in the list.

# Search for Fm definition to insert before it
if 'Fm=({value:e,label:t,color:r})' in content:
    # Check if b3e is already there
    if 'b3e=' not in content.split('Fm=')[0][-500:]:
        content = content.replace('Fm=({value:e,label:t,color:r})', original_b3e + 'Fm=({value:e,label:t,color:r})', 1)
        print("Restored b3e before Fm.")
    else:
        print("b3e already seems present before Fm.")
else:
    print("Fm signature not found.")

# 3. Ensure Fm width
# Fm context in v21: `className:"flex flex-col items-center justify-end h-full w-24 mx-3 group"`
# This is ALREADY w-24 per Jump 778. Good.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
