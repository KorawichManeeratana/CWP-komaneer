#!/usr/bin/env python3

def greetings(name:str = None):
    if name is None:
        print("Hello, noble stranger.")
    elif type(name) is not str:
        print( "Error! It was not a name.")
    else:
        print("Hello, " + name + ".")


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
