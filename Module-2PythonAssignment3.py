#Q3.  Compare and contrast mutable and immutable objects in Python with examples
list = [1, 2, 3]
list.append(4)
print(list) 

list.insert(1, 5)
print(list) 

list.remove(2)
print(list) 

popped_element = list.pop(0)
print(list)         
print(popped_element)  
