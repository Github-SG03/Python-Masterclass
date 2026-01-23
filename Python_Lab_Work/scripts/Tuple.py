############################Python programs for Tuples##########################
# Creating an empty tuple  
empty_tuple = ()
print('simple tuple:',empty_tuple)
  


# Creating tuple without parentheses  
single_tuple = "Tuple",
print(single_tuple)

# Creating a tuple that has only one element  
single_tuple = (10,)  
print( type(single_tuple) )   



#creating a tuple with some element
mixed_tuple = (4, "Python", 9.3)  
print("Tuple with different data types: ", mixed_tuple) 


#creating a tuple with nested sequence type
# Creating a nested tuple  
nested_tuple = ("Python", [1,2,3,4],{4: 5, 6: 2, 8:2}, (5, 3, 5, 6),{"Ravi","Suraj"})  
print("A nested tuple: ", nested_tuple)  


#accessing a tuple element 
nested_tuple = ("Tuple", [4, 6, 2, 6], (6, 2, 6, 7))   
# Accessing the index of a nested tuple  
print(nested_tuple[0][2])         
print(nested_tuple[1][1]) 
print(nested_tuple[2][1]) 


# Python program to show how slicing works in Python tuples    
# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")    
# Using slicing to access elements of the tuple  
print("Elements between indices 1 and 3: ", tuple_[1:3])    
# Using negative indexing in slicing  
print("Elements between indices 0 and -4: ", tuple_[:-4])    
# Printing the entire tuple by using the default start and end values.   
print("Entire tuple: ", tuple_[:]) 


#deleteing an entire tuple(as we cannot delete the tuple element since it is immutable)
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects","datatpe")
print(tuple_) 
del tuple_ 
#print(tuple_)   


# Python program to show how to tuple methods (.index() and .count()) work     
# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Ordered")     
# Counting the occurrence of an element of the tuple using the count() method  
print(tuple_.count('Ordered'))    
# Getting the index of an element using the index() method  
print(tuple_.index('Ordered')) # This method returns index of the first occurrence of the element  
print(tuple_.__doc__)

#Tuple built-in function
l = [1,-3,0,2,4]
print(all(ele > 0 for ele in l))#all() returns true if all the elements in(iterable(list,tuple,dictionary,string) is true)
m=[True, False, False]#print True if any one of the element is true
print(m)
my_set = {1, 2, 3, 4, 5}
total = sum(my_set) #sum all the element of iterable
print(total) 
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
# creating enumerate objects(provide iterator &element pair)
obj1 = enumerate(l1)
obj2 = enumerate(s1)
print ("Return type:", type(obj1))
print (list(enumerate(l1)))
l3=dict(enumerate(l1))
print(l3)
 
 
 
# changing start index to 2 from 0
print (list(enumerate(s1, 2)))
#converting list(any sequence type) to tuple
thistuple = tuple(["apple", "banana", "cherry"])
print(type(["apple", "banana", "cherry"]))
print(type(thistuple))

## tuple operation
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2#concatenating tuple
print(tuple3)
# Repeting the tuple elements  
tuple_ = tuple_ * 3# multiplying the entire tuple
print("New tuple is: ", tuple_)
# In/not in operator  
print('Tuple' in tuple_)  
print('Items' in tuple_)    
# Not in operator  
print('Immutable' not in tuple_)  
print('Items' not in tuple_)  

tuple_ = ("Python", "Tuple", "Ordered", "Immutable")    
# Iterating over tuple elements using a for loop  
for item in tuple_:  
    print(item)  
    
    
# But inside a tuple, we can change elements of a mutable object
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", [1,2,3,4])    
tuple_[-1][2] = 10# we can change tuple element if it has mutable objects 
print(tuple_)   
# Changing the whole tuple  
tuple_ = ("Python", "Items")  
print(tuple_)  
#changing tuple through list way
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#unpacking in the tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

