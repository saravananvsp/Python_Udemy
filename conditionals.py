try:
    a = int(input("Enter a number: "))

    if a == 5:
        print("equal to 5")
    elif a > 5:
        print("greater than 5")
    else:
        print("less than 5")

except ValueError:
    print("Enter a Valid Number!")