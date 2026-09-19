#!/usr/bin/env python3
base=float(__import__("sys").argv[1])
for m in (0.6,1.0,1.4): print(f"${round(base*m):.0f}")
