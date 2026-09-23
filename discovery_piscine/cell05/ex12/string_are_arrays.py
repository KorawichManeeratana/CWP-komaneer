#!/usr/bin/env python3

import sys

znum = sys.argv[1].count("z")

if znum == 0:
    print("none")
else:
    print("z" * znum)
