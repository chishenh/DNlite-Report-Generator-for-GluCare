
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-22.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Sentinel 1: E3e block
# find start of E3e
idx_e3e = content.find('E3e=({value:e,threshold:t=7.53,max:r=300})=>{')
idx_uk = content.find('Uk=({data:e,logo:t,companyLogo:r,inspector:n})=>{')

if idx_e3e != -1 and idx_uk != -1:
    print(f"Restoring E3e block (length removed: {idx_uk - idx_e3e})")
    golden_e3e = 'E3e=({value:e,threshold:t=7.53,max:r=300})=>{const n=typeof e=="number"&&!isNaN(e)?e:0,a=Math.log(1),i=Math.log(r),s=Math.max(1,Math.min(n,r)),o=Math.log(s),c=Math.log(t),f=i-a,h=(o-a)/f,d=(c-a)/f,g=85,p=105,y=140,v=77,b=-180,I=0,_=180,C=b+d*_,T=b+h*_,k=(W,te,Z,ce)=>{const Fe=ce*Math.PI/180;return{x:W+Z*Math.cos(Fe),y:te+Z*Math.sin(Fe)}},N=(W,te,Z,ce,Fe)=>{const ze=k(W,te,Z,Fe),_e=k(W,te,Z,ce),Se=Fe-ce<=180?"0":"1";return["M",ze.x,ze.y,"A",Z,Z,0,Se,0,_e.x,_e.y].join(" ")},Q=65,O=5,L=T*Math.PI/180,U=y+Q*Math.cos(L),Y=p+Q*Math.sin(L),S=y+O*Math.cos(L-Math.PI/2),H=p+O*Math.sin(L-Math.PI/2),z=y+O*Math.cos(L+Math.PI/2),ie=p+O*Math.sin(L+Math.PI/2),ee=`M ${S} ${H} L ${U} ${Y} L ${z} ${ie} Z`,re=N(y,p,g,b,C),ye=N(y,p,g,C,I),le=N(y,p,v,b,I),V=[1,3,10,30,100,300].map(W=>{const Z=(Math.log(W)-a)/f,ce=b+Z*_,Fe=k(y,p,v,ce),ze=k(y,p,v-5,ce),_e=k(y,p,v-15,ce);return{value:W,start:Fe,end:ze,textPos:_e}});return me.jsxs(Vf,{width:"280",height:"130",viewBox:"0 0 280 130",children:[me.jsx(Gd,{d:re,stroke:Br.teal,strokeWidth:16,fill:"none"}),me.jsx(Gd,{d:ye,stroke:Br.red,strokeWidth:16,fill:"none"}),me.jsx(Gd,{d:le,stroke:"black",strokeWidth:1,fill:"none"}),V.map((W,te)=>me.jsxs(Gk,{children:[me.jsx(Sb,{x1:W.start.x,y1:W.start.y,x2:W.end.x,y2:W.end.y,stroke:"black",strokeWidth:1}),me.jsx(ur,{x:W.textPos.x,y:W.textPos.y+3,textAnchor:"middle",fontSize:"8",fill:Br.slate600,children:String(W.value)})]},te)),me.jsx(Gd,{d:ee,fill:Br.needle}),me.jsx(Db,{cx:y,cy:p,r:5,fill:Br.needle})]})},'
    content = content[:idx_e3e] + golden_e3e + content[idx_uk:]
else:
    print("Sentinel 1 (E3e/Uk) fail.")

# Sentinel 2: b3e block
# Refresh indices after first replacement
idx_b3e = content.find('b3e=({value:e,threshold:t=7.53,max:r=300})=>{')
idx_fm = content.find('Fm=({value:e,label:t,color:r})=>')

if idx_b3e != -1 and idx_fm != -1:
    print(f"Restoring b3e block (length removed: {idx_fm - idx_b3e})")
    golden_b3e = 'b3e=({value:e,threshold:t=7.53,max:r=300})=>{const n=typeof e=="number"&&!isNaN(e)?e:0,a=Math.log(1),i=Math.log(r),s=Math.max(1,Math.min(n,r)),o=Math.log(s),c=Math.log(t),f=i-a,h=(o-a)/f,d=(c-a)/f,g=80,p=100,y=-180,v=0,b=180,I=y+d*b,_=y+h*b,C=(ie,ee,re,ye)=>{const le=ye*Math.PI/180;return{x:ie+re*Math.cos(le),y:ee+re*Math.sin(le)}},T=(ie,ee,re,ye,le)=>{const be=C(ie,ee,re,le),V=C(ie,ee,re,ye),W=le-ye<=180?"0":"1";return["M",be.x,be.y,"A",re,re,0,W,0,V.x,V.y].join(" ")},k=g-8,N=6,Q=_*Math.PI/180,O=p+k*Math.cos(Q),L=p+k*Math.sin(Q),U=p+N*Math.cos(Q-Math.PI/2),Y=p+N*Math.sin(Q-Math.PI/2),S=p+N*Math.cos(Q+Math.PI/2),H=p+N*Math.sin(Q+Math.PI/2),z=`M ${U} ${Y} L ${O} ${L} L ${S} ${H} Z`;return me.jsx("div",{style:{width:"300px",height:"160px",margin:"0 auto",position:"relative"},children:me.jsxs("svg",{width:"300",height:"160",viewBox:"0 0 200 110",xmlns:"http://www.w3.org/2000/svg",style:{overflow:"visible"},children:[me.jsx("path",{d:T(p,p,g,y,I),fill:"none",stroke:V0.teal,strokeWidth:"16"}),me.jsx("path",{d:T(p,p,g,I,v),fill:"none",stroke:V0.red,strokeWidth:"16"}),me.jsx("text",{x:C(p,p,g+20,I).x,y:C(p,p,g+20,I).y,textAnchor:"middle",fontSize:"10",fill:"#64748b",fontWeight:"bold",children:t}),me.jsx("text",{x:C(p,p,g+20,y).x,y:C(p,p,g+20,y).y+5,textAnchor:"start",fontSize:"10",fill:"#94a3b8",children:"1"}),me.jsx("text",{x:C(p,p,g+20,v).x,y:C(p,p,g+20,v).y+5,textAnchor:"end",fontSize:"10",fill:"#94a3b8",children:"300"}),me.jsx("path",{d:z,fill:V0.needle}),me.jsx("circle",{cx:p,cy:p,r:5,fill:V0.needle})]})})},'
    content = content[:idx_b3e] + golden_b3e + content[idx_fm:]
else:
    print("Sentinel 2 (b3e/Fm) fail.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
