
import os

file_path = 'c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-8.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- Part 1: Excel Parsing ---
# Target: `U._unit=U[Y("單位")]||U[Y("Unit")]||U[Y("Clinic")]||"GluCare. Health"`
# We want to insert `U._diabetic=U[Y("Diabetic")]||"Yes",` before or after.
# Let's target `U._unit=` start.
target_parse = 'U._unit=U[Y("單位")]'
repl_parse = 'U._diabetic=U[Y("Diabetic")]||"Yes",U._unit=U[Y("單位")]'

content_v1 = content.replace(target_parse, repl_parse)
if content_v1 == content:
    print("Error: Excel parsing patch failed")
else:
    print("Excel parsing patch applied.")

# --- Part 2: Definition of Risk Logic ---
# Logic: const isDM = (i._diabetic||"").toLowerCase() !== "no"; (But we need to inject this or use inline)
# Inline: `(String(i._diabetic||"").toLowerCase()!=="no")`

# Text 1: "9.5 times" section (Renal Function Deterioration)
# Target: `children:["If your DNlite level is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"High Risk"}),", your risk of renal function deterioration within 5 years is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"9.5 times"})," higher than that of a diabetic patient."]`
# We need to make the "9.5 times" variable and "diabetic patient" variable.
# OR switch entire block.
# Switching entire block is cleaner.
# `children:(String(i._diabetic||"").toLowerCase()!=="no" ? [...] : [...])`

# The minified code uses `children:[ ... ]` array.
# I will replace the array content `[...]` with logic.
# But `children:` expects a node or array. ternary returns array.
# Let's find the exact string boundaries.
start_str = 'children:["If your DNlite level is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"High Risk"}),", your risk of renal function deterioration within 5 years is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"9.5 times"})," higher than that of a diabetic patient."]'

# DM Block (Existing)
block_dm = '["If your DNlite level is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"High Risk"}),", your risk of renal function deterioration within 5 years is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"9.5 times"})," higher than that of a diabetic patient."]'

# Non-DM Block
# "If your DNlite level is High Risk, your risk of renal function deterioration within 5 years is 4.0 times higher than that of the general population."
block_non_dm = '["If your DNlite level is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"High Risk"}),", your risk of renal function deterioration within 5 years is ",me.jsx(ur,{style:{color:Br.red,fontFamily:"Helvetica-Bold"},children:"4.0 times"})," higher than that of the general population."]'

# Replacement logic
repl_risk_deterioration = f'(String(i._diabetic||"").toLowerCase()!=="no" ? {block_dm} : {block_non_dm})'

content_v2 = content_v1.replace(block_dm, repl_risk_deterioration)
if content_v2 == content_v1:
    print("Error: Risk Deterioration patch failed")

# Text 2: ESRD (3.5 times vs 1.6 times)
# Identify pattern from dump... check if I have it. I requested "9.5 times" context, but "3.5 times" is usually next.
# I might need to dump "3.5 times" to be sure of exact string.
# Let's assume structure is similar but replaced 9.5 with 3.5. But "diabetic patient" phrase might be there too.

# --- Part 3: Important Notes / Risk Mark ---
# This is the long text in `me.jsx("p",{className... children: N ? "..." : "..."})`
# `N` is likely the 'isHighRisk' boolean (High vs Low). 
# Dump context 2231927 showed: `children:N?"Your kidney function is in <LowRiskText>":"<HighRiskText>"` 
# Actually logic usually is `conditions ? trueVal : falseVal`.
# `children:N?"HighRiskText":"LowRiskText"` (Typical)
# Let's check text: "Your kidney function is in a condition that may negatively impact..." (High Risk text).
# "Your kidney function is within the normal range..." (Low Risk text).
# Wait, user request lists Low Risk first? "Low Risk: ... High Risk: ..."
# But code `N` usually implies `isHighRisk`.
# If `N` is true -> High Risk.
# The dump says `N?"Your kidney function... impact your health...":"Your kidney function... normal range..."`
# So N is High Risk.

# DM High: "If you have type 2 diabetes... 9.5 times... 3.5 times..."
# Non-DM High: "If you do not have diabetes... 4 times... 1.6 times..."
# DM Low == Non-DM Low (from user text "Your kidney function is within the normal range...").

# So we need to change the High Risk string to be conditional.
# `children:N ? (isDM ? "DM High Text" : "Non-DM High Text") : "Low Risk Text"`

# I need the exact strings from the file to replace them.
# I'll create a script to dump these exact strings first, to ensure 100% match.

