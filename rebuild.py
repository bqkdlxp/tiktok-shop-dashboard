#!/usr/bin/env python3
"""Rebuild index.html with fresh embedded data from generate_real_data.py"""
import subprocess, sys

# Step 1: Generate fresh data
subprocess.run([sys.executable, 'generate_real_data.py'], check=True)

# Step 2: Read new data.js
with open('data.js') as f:
    new_data = f.read()

# Step 3: Read index.html, find and replace inline data block
with open('index.html') as f:
    html = f.read()

# Find the inline data section: starts with // TikTok Shop, ends with var DATA_LOADED
import re
pattern = r'var PRODUCTS = \[.*?var DATA_LOADED = true;\n'
replacement = new_data.replace('var TIME_SERIES = [];\n', '').strip()
html = re.sub(pattern, replacement, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

print('✅ index.html rebuilt with fresh data')
