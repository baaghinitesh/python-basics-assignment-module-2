#Q5. explain the concept of type casting in Python with examples.

#Explicit type casting
string = "56"
number = 44

# Converting the string into an integer number.
number1 = int(string)

number2 = number + number1
print("The Sum of both the numbers is: ", number2)
 
# implicit type Casting 

# Python automatically converts a to int 
a = 7
print(type(a)) 

# Python automatically converts b to float 
b = 3.0
print(type(b)) 

# Python automatically converts c to float as it is a float addition 
c = a + b 
print(c) 
print(type(c))

# Python automatically converts d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))
