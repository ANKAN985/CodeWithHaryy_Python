# Pattern Printing
# Input = integer n
# Boolean = take as 0 or 1 and cast it to boolean
# If True then print
# *
# **
# ***
# ****
# If False then print
# ****;
# ***
# **
# *
num = int(input("Enter a number:\n"))
while True:
    choice = input("Enter 0 or 1:\n")
    if choice not in ['0', '1']:
        print("Please enter a valid choice!")
        continue
    else:
        if choice == '1':
            choice = True
        else:
            choice = False

        if not choice:
            for i in range(num, 0, -1):
                for j in range(0, i):
                    print("*", end="")
                print()
            break
        else:
            for i in range(0, num + 1):
                for j in range(0, i):
                    print("*", end="")
                print()
            break
