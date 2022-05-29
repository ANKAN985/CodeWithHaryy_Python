# Exercise 2 - Faulty Calculator

"""
First, take input about the operation
then, ask the two numbers
Except the following, all other answers should be correct

45 * 3 = 555, 56 + 9 = 77, 56/6 = 4
"""

choice = int(input("Enter 1 for sum, 2 for subtraction, 3 for multiplication and 4 for division: "))
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 < num2 and choice in [1, 3]:
    num1, num2 = num2, num1

if num1 == 45 and num2 == 3 and choice == 3:
    print("Result is: ", "555")
elif num1 == 56 and num2 == 9 and choice == 1:
    print("Result is: ", "77")
elif num1 == 56 and num2 == 6 and choice == 4:
    print("Result is: ", "4")
else:
    if choice == 1:
        print("Result is: ", num1 + num2)
    elif choice == 2:
        print("Result is: ", num1 - num2)
    elif choice == 3:
        print("Result is: ", num1 * num2)
    elif choice == 4:
        print("Result is: ", num1 / num2)
    else:
        print("Wrong choice of operation!")
