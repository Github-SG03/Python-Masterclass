#1.Python program to get the Unicode of the character
print(chr(97))
# Output: a
print(chr(98))
#  Output: b

############################################################################################################                                      

#2.Python program to get the Binary of the character
number = 5 
# convert 5 to its binary equivalent
print('The binary equivalent of 5 is:', bin(number))

############################################################################################################                                      

#3.Python program to get the Ascii of the character
text = 'Pythön is interesting'
# replace ö with its ascii value
print(ascii(text))    # Output: 'Pyth\xf6n is interesting' 
c = 'g'
# print the ASCII value of assigned character in c
print("The ASCII value of",c,"is", ord(c))

############################################################################################################                                      
#4.Python program to get the 'all' the elemnts are truth or not
boolean_list = ['True', 'True', 'True']
# check if all elements are true
result = all(boolean_list)
print(result)
# Output: True

############################################################################################################                                      
#5.Python program to get the 'any' the elemnts are truth or not
boolean_list = ['True', 'False', 'True']

# check if any element is true
result = any(boolean_list)
print(result)
# Output: True

############################################################################################################
#6.Python program to get the absolute value of a number
number = -20
absolute_number = abs(number)
print(absolute_number)
# Output: 20


############################################################################################################
#7.Python program to get the round off value of a number
number = 13.46
# round 13.46 to the nearest integer
rounded_number = round(number)
print(rounded_number)
# Output: 13

############################################################################################################
#8.Python program to get range value of a number
# create a sequence from 0 to 3
numbers = range(4)

# iterating through the sequence
for i in numbers:
    print(i)
    

############################################################################################################
#9.Python program to get the type of a number
prime_numbers = [2, 3, 5, 7]

# check type of prime_numbers
result = type(prime_numbers)
print(result)

# Output: <class 'list'>

############################################################################################################
#10.Python program to import the module of
mathematics = __import__('math', globals(), locals(), [], 0)
print(mathematics.fabs(-2.5))
# Output: 2.5

############################################################################################################
#11.Python program to get the boolean value of a number
test1 = 1
test2=0
# returns boolean value of 1
print(test1, 'is', bool(test1))
print(test2, 'is', bool(test2))
# Output: 1 is True
# Output: 0 is False

############################################################################################################
#12.Python program to get the complex value of a number
z = complex(2, -3)
print(z)

z = complex(1)
print(z)

z = complex()
print(z)

z = complex('5-9j')
print(z)
# Output: (2-3j)
# Output: (1+0j)
# Output: 0j
# Output: (5-9j)

############################################################################################################
#13.Python program to get the callable value of a number
x = 5
print(callable(x))

def testFunction():
  print("Test")

y = testFunction
print(callable(y))

# Output: False
# Output: True

############################################################################################################
#14.Python program to get the valid attributes of a number
number = [12]
# returns valid attributes of the number list 
print(dir(number))
# Output: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

############################################################################################################
#15.Python program to get the object value of a number
test = object()
print(type(test))
print(dir(test))

# Output: <class 'object'>
# Output: ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

############################################################################################################
#16.Python program to get the next value of a number
marks = [65, 71, 68, 74, 61]

# convert list to iterator
iterator_marks = iter(marks)

# the next element is the first element
marks_1 = next(iterator_marks)
print(marks_1)

# find the next element which is the second element
marks_2 = next(iterator_marks)
print(marks_2)

# Output: 65
#         71

############################################################################################################
#17.Python program to get the map value of an iterable item
numbers = [1,2,3,4]
# returns the square of a number
def square(number):
  return number * number

# apply square() to each item of the numbers list
squared_numbers = map(square, numbers)

# converting to list for printing
result = list(squared_numbers)
print(result) 

# Output: [1,4,9,16]

############################################################################################################
#18.Python program to get the local variables and symblols of a number
print(locals())


############################################################################################################
#19.Python program to get a unique integer (identity) of a passed argument object
a = 5
b = 6
sum = a + b

# id of sum variable
print("The id of sum is", id(sum))

# Output: The id of sum is 9789312

############################################################################################################
#20.Python program to get the hash value of a text
text = 'Python Programming'

# compute the hash value of text
hash_value = hash(text)
print(hash_value)

# Output: -966697084172663693

############################################################################################################
#21.Python program to get the help value of an object
list = [1, 2, 3, 4]
print(help(list))

############################################################################################################
#22.Python program to execute dynamically created program
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)

# Output: Sum = 15

############################################################################################################
#23.Python program to get the formatted value of a number
# decimal formatting
decimal_value = format(123, 'd')

print("Decimal Formatting:", decimal_value)

# binary formatting
binary_value = format(123, 'b')

print("Binary Formatting:", binary_value)
# Output: Decimal Formatting: 123
# Output: Binary Formatting: 1111011

############################################################################################################
#24.Python program to get the eval value of a number
x = 1
print(eval('x + 1'))

# Output: 2

############################################################################################################
#25.selects elements from an iterable based on the result of a function.
# returns True if the argument passed is even
def check_even(number):
    if number % 2 == 0:
          return True  
    return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# if an element passed to check_even() returns True, select it
even_numbers_iterator = filter(check_even, numbers)

# converting to list
even_numbers = list(even_numbers_iterator)
print(even_numbers)

# Output: [2, 4, 6, 8, 10]

############################################################################################################
#26.Python program to get the divmod value of a number
# returns the quotient and remainder of 8/3
result = divmod(8, 3)

print('Quotient and Remainder = ',result)

# Output: Quotient and Remainder =  (2, 2)

############################################################################################################
#27.Python program to get the class value of a number
class Calculator:

  def add_numbers(num1, num2):
    return num1 + num2

# convert add_numbers() to static method
Calculator.add_numbers = staticmethod(Calculator.add_numbers)

sum = Calculator.add_numbers(5, 7)
print('Sum:', sum)

# Output: Sum: 12

############################################################################################################








