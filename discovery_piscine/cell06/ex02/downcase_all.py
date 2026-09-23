#!/usr/bin/env python3

import sys

def downcase_it(word: str):
    return word.lower()

def main():
    for i in range(1, len(sys.argv)):
        print(downcase_it(sys.argv[i]))

main()