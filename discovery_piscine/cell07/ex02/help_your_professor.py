#!/usr/bin/env python3

def average(students: dict):
    total = 0
    for student in students:
        total += students[student]
    return total / len(students)



def main():
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
    }
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
    }

    print("Average for class 3B:", str(average(class_3B))+".")
    print("Average for class 3C:", str(average(class_3C))+".")


main()