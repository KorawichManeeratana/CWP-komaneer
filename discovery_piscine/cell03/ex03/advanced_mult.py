for i in range(0, 11):
    count = 1
    print("Table de " + str(i) +": ", end="")
    while count < 10:
        print(i*count, end=" ")
        count += 1
    print()