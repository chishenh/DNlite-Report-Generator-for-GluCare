
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-22.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Sentinel 2: b3e block replacement with ENHANCED version
idx_b3e = content.find('b3e=({value:e,threshold:t=7.53,max:r=300})=>{')
idx_fm = content.find('Fm=({value:e,label:t,color:r})=>')

if idx_b3e != -1 and idx_fm != -1:
    print(f"Applying enhanced b3e (length to replace: {idx_fm - idx_b3e})")
    
    # Enhanced b3e logic: Includes the black inner arc and markers. 
    # Adapted from PDF's E3e but for HTML DOM.
    enhanced_b3e = (
        'b3e=({value:e,threshold:t=7.53,max:r=300})=>{'
        'const n=typeof e=="number"&&!isNaN(e)?e:0,a=Math.log(1),i=Math.log(r),s=Math.max(1,Math.min(n,r)),o=Math.log(s),c=Math.log(t),f=i-a,h=(o-a)/f,d=(c-a)/f,'
        'g=85,p=105,y=135,v=77,b=-180,I=0,_=180,C=b+d*_,T=b+h*_,k=(W,te,Z,ce)=>{const Fe=ce*Math.PI/180;return{x:W+Z*Math.cos(Fe),y:te+Z*Math.sin(Fe)}},'
        'N=(W,te,Z,ce,Fe)=>{const ze=k(W,te,Z,Fe),_e=k(W,te,Z,ce),Se=Fe-ce<=180?0:1;return["M",ze.x,ze.y,"A",Z,Z,0,Se,0,_e.x,_e.y].join(" ")},'
        'Q=65,O=5,L=T*Math.PI/180,U=y+Q*Math.cos(L),Y=p+Q*Math.sin(L),S=y+O*Math.cos(L-Math.PI/2),H=p+O*Math.sin(L-Math.PI/2),z=y+O*Math.cos(L+Math.PI/2),ie=p+O*Math.sin(L+Math.PI/2),'
        'ee=`M ${S} ${H} L ${U} ${Y} L ${z} ${ie} Z`,re=N(y,p,g,b,C),ye=N(y,p,g,C,I),le=N(y,p,v,b,I),'
        'V=[1,3,10,30,100,300].map(W=>{const Z=(Math.log(W)-a)/f,ce=b+Z*_,Fe=k(y,p,v,ce),ze=k(y,p,v-5,ce),_e=k(y,p,v-15,ce);return{value:W,start:Fe,end:ze,textPos:_e}});'
        'return me.jsx("div",{style:{width:"280px",height:"130px",margin:"0 auto",position:"relative"},children:me.jsxs("svg",{width:"280",height:"130",viewBox:"0 0 280 130",xmlns:"http://www.w3.org/2000/svg",style:{overflow:"visible"},'
        'children:[me.jsx("path",{d:re,stroke:V0.teal,strokeWidth:16,fill:"none"}),me.jsx("path",{d:ye,stroke:V0.red,strokeWidth:16,fill:"none"}),'
        'me.jsx("path",{d:le,stroke:"black",strokeWidth:1,fill:"none"}),'
        'V.map((W,te)=>me.jsxs("g",{children:[me.jsx("line",{x1:W.start.x,y1:W.start.y,x2:W.end.x,y2:W.end.y,stroke:"black",strokeWidth:1}),'
        'me.jsx("text",{x:W.textPos.x,y:W.textPos.y+3,textAnchor:"middle",fontSize:"8",fill:"#64748b",children:String(W.value)})]},te)),'
        'me.jsx("path",{d:ee,fill:V0.needle}),me.jsx("circle",{cx:y,cy:p,r:5,fill:V0.needle})]})})},'
    )
    
    content = content[:idx_b3e] + enhanced_b3e + content[idx_fm:]
    print("Enhanced b3e applied successfully.")
else:
    print("b3e/Fm sentinel mismatch. Aborting.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
