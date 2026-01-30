
import os

base_dir = os.getcwd()
file_path = os.path.join(base_dir, 'assets', 'index-patched-32.js')

print(f"Reading {file_path}")

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Verify Parsing Logic
    expected_parsing = 'U[Y("Lab. Director")]||U[Y("Lab Director")]'
    if expected_parsing in content:
        print("[PASS] Parsing logic patch verified.")
    else:
        print("[FAIL] Parsing logic patch NOT found.")

    # Verify HTML Rendering
    expected_html = 'children:g._inspector})'
    if expected_html in content:
        print("[PASS] HTML rendering patch verified.")
    else:
        print("[FAIL] HTML rendering patch NOT found.")

except Exception as e:
    print(f"Error reading file: {e}")
