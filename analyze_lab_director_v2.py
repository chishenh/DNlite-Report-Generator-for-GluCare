
import os

# Use current working directory resolution
base_dir = os.getcwd()
file_path = os.path.join(base_dir, 'assets', 'index-patched-31.js')

print(f"Reading {file_path}")

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    search_terms = ["Lab Director", "Lab. Director"]
    
    for term in search_terms:
        print(f"\nSearching for '{term}'...")
        start = 0
        matches = []
        while True:
            idx = content.find(term, start)
            if idx == -1:
                break
            matches.append(idx)
            start = idx + 1
        
        print(f"Found {len(matches)} matches for '{term}'")
        
        for i, idx in enumerate(matches):
            print(f"--- Match {i+1} at {idx} ---")
            # Show more context before and after
            s = max(0, idx - 200)
            e = min(len(content), idx + 200)
            context = content[s:e]
            print(context)
            
except Exception as e:
    print(f"Error: {e}")
