#!/usr/bin/env python3
"""Rebuild index.html with fresh embedded data from generate_real_data.py"""
import subprocess, sys, random
from datetime import datetime

# Step 1: Generate fresh data with today's date as random seed
today = datetime.now().strftime('%Y%m%d')
# Patch the seed in generate_real_data.py before running
with open('generate_real_data.py') as f:
    gen_code = f.read()

# Replace seed with today's date so data changes daily
import re
gen_code = re.sub(r'random\.seed\(\d+\)', f'random.seed({today})', gen_code)

with open('gen_today.py', 'w') as f:
    f.write(gen_code)

subprocess.run([sys.executable, 'gen_today.py'], check=True)

# Step 2: Read new data.js
with open('data.js') as f:
    new_data = f.read()

# Step 3: Read index.html, replace inline data block
with open('index.html') as f:
    html = f.read()

pattern = r'var PRODUCTS = \[.*?var DATA_LOADED = true;\n'
replacement = new_data.strip()
html = re.sub(pattern, replacement, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

print('✅ index.html rebuilt with fresh data (seed={})'.format(today))
