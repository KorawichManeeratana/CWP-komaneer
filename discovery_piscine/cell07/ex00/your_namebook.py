#!/usr/bin/env python3

def array_of_name(dic : dict):
    name_list = []
    for key in dic:
        
        name_list.append(key.capitalize() + " " + dic[key].capitalize())
    return name_list

def main():
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }

    print(array_of_name(persons))

main()