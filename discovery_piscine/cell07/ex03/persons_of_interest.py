#!/usr/bin/env python3

def famous_births(scientists: dict):
    newsci = dict(sorted(scientists.items(), key=lambda x: x[1]["date_of_birth"]))
    for key in newsci:
        print(newsci[key]["name"] + " is a great scientist born in " + newsci[key]["date_of_birth"] + ".")


def main():
    women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }

    famous_births(women_scientists)

main()