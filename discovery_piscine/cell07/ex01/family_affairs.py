#!/usr/bin/env python3

def find_the_redheads(fam: dict):
    redheads_obj = filter(lambda x: x[1] == "red", fam.items())
    return [item[0] for item in redheads_obj]

def main():
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }

    print(find_the_redheads(dupont_family))

main()
