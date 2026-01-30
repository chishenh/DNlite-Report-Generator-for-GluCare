
import os

base_dir = r"c:\Users\BPM105004\DNlite-Report-Generator-for-GluCare"
js_file = os.path.join(base_dir, "assets", "index-patched-34.js")

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

search_term = "Normal Range"
start = 0
while True:
    try:
        idx = content.index(search_term, start)
        # Print context: 50 chars before and after
        print(f"Match at {idx}: ...{content[idx-50:idx+50]}...")
        start = idx + len(search_term)
    except ValueError:
        break
