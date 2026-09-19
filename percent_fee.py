#!/usr/bin/env python3
import sys
price=float(sys.argv[1]); fee=float(sys.argv[2]) if len(sys.argv)>2 else 0.129
print(round(price*(1-fee),2))
