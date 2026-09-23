#!/usr/bin/env python3

import sys
print("parameters: "+ str(len(sys.argv) - 1))
for i in range(1, len(sys.argv)):
    print(sys.argv[i] + ": " + str(len(sys.argv[i])))
