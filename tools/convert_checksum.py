#!/usr/bin/env python3

# This script converts Apache's weird checksum format into something that 
# sha512sum can read.

# Owain Kenway, 8th November 2021

import sys
from pathlib import Path

if len(sys.argv) < 2:
	sys.exit('Run with convert_checksum.py <file>.')

filename = sys.argv[1]

orig = Path(filename).read_text()

fixed_sha512 = orig.split(':')[1].replace(' ','').replace('\n','').lower()
fixed_file = orig.split(':')[0].strip()

print(fixed_sha512 + '  ' + fixed_file)
