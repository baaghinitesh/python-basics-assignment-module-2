#Q3.  Compare and contrast mutable and immutable objects in Python with examples 
  
tuple1 = (0, 1, 2, 3) 
tuple1[0] = 4 # tuples are immutable error
print(tuple1) 

message = "Hello world"
message[0] = 'p' # strings are immutable error
print(message)