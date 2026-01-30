
import os

base_dir = os.getcwd()
file_path = os.path.join(base_dir, 'assets', 'index-patched-32.js')

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the context where we applied the patch
# We replaced 'U[Y("Lab Director")]' with 'U[Y("Lab. Director")]||U[Y("Lab Director")]'
search_term = 'U[Y("Lab. Director")]'
idx = content.find(search_term)

if idx != -1:
    print(f"Found patch at {idx}")
    s = max(0, idx - 200)
    e = min(len(content), idx + 200)
    print("--- Parsing Logic Context ---")
    print(content[s:e])
else:
    print("Patch string not found in file!")
    
# Also check if there's any other "Lab Director" usage that might be relevant
print("\n--- Other 'Lab Director' occurrences ---")
start = 0
count = 0
while True:
    idx = content.find("Lab Director", start)
    if idx == -1:
        break
    if abs(idx - content.find(search_term)) > 100: # Don't reprint the one we just found
         print(f"Match at {idx}: {content[idx-50:idx+50]}")
    start = idx + 1
    count += 1
