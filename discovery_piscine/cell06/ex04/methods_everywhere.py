#!/usr/bin/env python3

import sys

def shrink(word: str):
    return word[0:8]

def enlarge(word: str):
    return word + "Z" * (8 - len(word))

def main():
    if len(sys.argv) < 2:
        print("none")
        return
    
    for i in range(1, len(sys.argv)):
        word = sys.argv[i]
        if len(word) > 8:
            print(shrink(word))
        elif len(word) < 8:
            print(enlarge(word))
        else:
            print(word)

main()