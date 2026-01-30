
import os

base_dir = os.getcwd()
file_path = os.path.join(base_dir, 'assets', 'index-patched-32.js')

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check where _disp_dnlite is pattern matched
# Expected: U._disp_dnlite = ... in parsing
# And C._disp_dnlite (or similar) in rendering

print("--- Searching for _disp_dnlite ---")
idxs = []
start = 0
while True:
    idx = content.find("_disp_dnlite", start)
    if idx == -1:
        break
    idxs.append(idx)
    start = idx + 1 # overlapping? no need

for i, idx in enumerate(idxs):
    print(f"Match {i+1} at {idx}")
    s = max(0, idx - 50)
    e = min(len(content), idx + 50)
    print(f"Context: {content[s:e]}") 

# Check if C matches g usage in proximity
print("\n--- Correlation of C and g ---")
# I want to see if C and g are used in the same block.
# I'll re-read the component context around the footer
search_context = 'className:"footer-section"'
c_idx = content.find(search_context)
if c_idx != -1:
    s = max(0, c_idx - 1000)
    e = min(len(content), c_idx + 1000)
    sub = content[s:e]
    # Simple check for C. and g.
    print(f"Occurrences of C. in footer context: {sub.count('C.')}")
    print(f"Occurrences of g. in footer context: {sub.count('g.')}")
    
