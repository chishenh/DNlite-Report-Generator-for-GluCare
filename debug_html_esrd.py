
import os
with open('c:/Users/BPM105004/Downloads/DNlite-Report-Generator-for-GluCare-gh-pages/assets/index-patched-9.js', 'r', encoding='utf-8') as f:
    c = f.read()
idx = c.find("developing ESRD within 5 years is")
if idx != -1:
    print("--- HTML ESRD ---")
    print(c[idx-200:idx+600])
