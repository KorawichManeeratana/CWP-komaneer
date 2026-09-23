#!/usr/bin/env python3

import sys

for i in range(1, len(sys.argv)):
    if sys.argv[i][-3:] != "ism":
        print(sys.argv[i] + "ism")