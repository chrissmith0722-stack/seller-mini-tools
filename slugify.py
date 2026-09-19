#!/usr/bin/env python3
import re,sys
s=sys.argv[1] if len(sys.argv)>1 else ""
print(re.sub(r"[^a-z0-9]+","-",s.lower()).strip("-"))
