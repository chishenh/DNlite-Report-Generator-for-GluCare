
import os

# Define paths
base_dir = r"c:\Users\BPM105004\DNlite-Report-Generator-for-GluCare"
assets_dir = os.path.join(base_dir, "assets")
current_js_file = os.path.join(assets_dir, "index-patched-34.js")
new_js_file = os.path.join(assets_dir, "index-patched-35.js")
index_html_file = os.path.join(base_dir, "index.html")

def patch_js():
    if not os.path.exists(current_js_file):
        print(f"Error: {current_js_file} not found.")
        return False

    with open(current_js_file, "r", encoding="utf-8") as f:
        content = f.read()

    # The specific string we want to replace
    # Based on earlier grep, it appears as "Normal Range: 0.60-2.50"
    # We will replace "Normal Range" with "Reference Range"
    
    # Check if target exists
    if "Normal Range" not in content:
        print("Error: 'Normal Range' string not found in file.")
        return False
        
    # Perform replacement
    new_content = content.replace("Normal Range", "Reference Range")
    
    # Verify replacement happened
    if "Reference Range" not in new_content:
        print("Error: Replacement failed internally.")
        return False

    with open(new_js_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"Created {new_js_file}")
    return True

def update_index_html():
    if not os.path.exists(index_html_file):
        print(f"Error: {index_html_file} not found.")
        return False

    with open(index_html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Replace reference
    new_html_content = html_content.replace("index-patched-34.js", "index-patched-35.js")

    if new_html_content == html_content:
        print("Warning: No changes made to index.html (maybe already updated?)")
    else:
        with open(index_html_file, "w", encoding="utf-8") as f:
            f.write(new_html_content)
        print("Updated index.html")

    return True

if __name__ == "__main__":
    if patch_js():
        update_index_html()
        print("Patch applied successfully.")
    else:
        print("Patch failed.")
