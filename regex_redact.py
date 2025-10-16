#!/usr/bin/env python3

import re
import argparse

# Usage ./regex_redact.py <file_name>

PATTERNS = {
	"DATE":re.compile(r"[0-9]{4}[-/][0-9]{1,2}[-/][0-9]{1,2}"),
	"PHONE NUMBER":re.compile(r"\+[0-9]+ ?[0-9]{3,4}+ ?[0-9]{3}+ ?[0-9]{3}"),
	"CREDIT CARD NUMBER":re.compile(r"[0-9]{4}+ ?[0-9]{4}+ ?[0-9]{4}+ ?[0-9]{4}"),
	"MAC ADDRESS":re.compile(r"[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}"),
	"UUID":re.compile(r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}"),
	"IP ADDRESS":re.compile(r"(25[0-5]|2{0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2{0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2{0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2{0-4][0-9]|[01]?[0-9]?[0-9])"),
	"EMAIL":re.compile(r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9._+-]+\.(com|org|net)")
}


parser = argparse.ArgumentParser()
parser.add_argument("input")
args = parser.parse_args()

with open(args.input) as filp:
	contents = filp.read()

for redaction_key, redaction_patterns in PATTERNS.items():
	contents = redaction_patterns.sub(
				f"[[ REDACTED {redaction_key} ]]", 
				contents)

print(contents)	