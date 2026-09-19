#!/usr/bin/env python3
import zipfile,sys
for n in zipfile.ZipFile(sys.argv[1]).namelist(): print(n)
