num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
mult = num1 * num2
print(str(num1) + " x " + str(num2) + " = " + str(mult))

if (mult == 0):
    print("The result is zero.")
elif (mult < 0):
    print("The result is negative.")
else:
    print("The result is positive.")