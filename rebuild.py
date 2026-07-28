#!/usr/bin/env python3
"""Rebuild index.html with fresh embedded data"""
import subprocess, sys, re
from datetime import datetime

# Step 1: Generate fresh data with today's date as seed
today = int(datetime.now().strftime('%Y%m%d'))
# Set seed via env var (generate_real_data.py checks RANDOM_SEED)
import os
os.environ['RANDOM_SEED'] = str(today)
subprocess.run([sys.executable, 'generate_real_data.py'], check=True)

# Step 2: Read new data.js and replace inline data in index.html
with open('data.js') as f:
    new_data = f.read()
with open('index.html') as f:
    html = f.read()

html = re.sub(
    r'var PRODUCTS = \[.*?var DATA_LOADED = true;',
    new_data.strip() + '\n',
    html, flags=re.DOTALL
)
with open('index.html', 'w') as f:
    f.write(html)

print(f'✅ Rebuilt (seed={today})')
