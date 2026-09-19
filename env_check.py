#!/usr/bin/env python3
import os,sys
missing=[k for k in sys.argv[1:] if not os.environ.get(k)]
print("OK" if not missing else "MISSING: "+",".join(missing)); raise SystemExit(1 if missing else 0)
