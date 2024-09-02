#Q6. How do conditional statements wok in Python? Illustrate with examples

# if statement example
if 10 > 5:
    print("10 greater than 5")

print("Program ended")

# if..else statement example
x = 3
if x == 4:
    print("Yes")
else:
    print("No")


# if..else chain statement
letter = "A"

if letter == "B":
    print("letter is B")

else:

    if letter == "C":
        print("letter is C")

    else:

        if letter == "A":
            print("letter is A")

        else:
            print("letter isn't A, B and C")

# if-elif statement example
letter = "A"

if letter == "B":
    print("letter is B")

elif letter == "C":
    print("letter is C")

elif letter == "A":
    print("letter is A")

else:
    print("letter isn't A, B or C")


