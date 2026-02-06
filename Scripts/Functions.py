############################################Function in python_tutorial####################################################


#Example1 of a User-Defined Function
#We will define a function that when called will return the square of the number passed to it as an argument.
def square( num ):  #function definition
    """ 
    This function computes the square of the number. 
    """  
    return num**2 
object_ = square(9) #function call 
print( "The square of the number is: ", object_ )


#Example2 of a User-Defined Function
#calling a function from print(), function can be called from anywhere in program
def a_function( string ):  
    "This prints the value of length of string"  
    return len(string)  
#Calling the function we defined  
print( "Length of the string Functions is: ", a_function( "Functions" ) )  
print( "Length of the string python_tutorial is: ", a_function( "python_tutorial" ) ) 

#Example3  of a User-Defined Function







##############################################################################################################################################

#way to call function
#Caliing a function by 'Pass by Reference VS Pass by Value'
def square( my_list ): #defining the function 
    '''''This function will find the square of items in list'''  
    squares = []  
    for l in my_list:  
      squares.append( l**2 )  
      return squares  
list_ = [45, 52, 13] 
result = square( list_ )  # calling the defined function by 'Pass by Reference'
print( "Squares of the list is: ", result ) 

##################################################################################################################################################


##Function Arguments(calling a function through Pass by Value)
#1.Default Arguments(takes default value when no value is defined in function call)
def function( num1, num2 = 40 ):  
   print("num1 is: ", num1)  
   print("num2 is: ", num2)  
print( "Passing one argument",function(10))# Calling the function and passing only one argument    
print( "Passing two arguments",function(10,30)) # Now giving two arguments to the function
#2.Keyword Arguments()
def function( num1, num2 ):  
   print("num1 is: ", num1)  
   print("num2 is: ", num2)  
print( "Without using keyword",function( 50, 30)  )  # Calling function and passing arguments without using keyword  
print( "With using keyword",function( num2 = 50, num1 = 30))# Calling function and passing arguments using keyword  
#3Variable-Length Arguments(We can use special characters in python_tutorial functions to pass as many arguments as we want in a function. There are two types of characters that we can use for this purpose:1.*args,2.**Kwargs)
#3.1*args(non-keyword arguments)
def function( *args_list ):  
   ans = []  
   for l in args_list:  
       ans.append( l.upper() ) 
   return ans  
object = function('python_tutorial', 'Functions', 'tutorial')# Passing args arguments   
print( object )  
#3.2**kwargs(keywords arguments)
def function( **kargs_list ):  
    ans = []  
    for key, value in kargs_list.items(): 
        ans.extend([key, value])  
    return ans  
object = function(First = "python_tutorial", Second = "Functions", Third = "Tutorial") # Paasing kwargs arguments  
print(object) 
#4Required Arguments()
def function( num1, num2 ): 
    print("num1 is: ", num1) 
    print("num2 is: ", num2)  
print( "Passing out of order arguments" ,function( 30, 20 ) )  # Calling function and passing two arguments out of order, we need num1 to be 20 and num2 to be 30  
try:
   print( "Passing only one argument",function( 30 ) )  # Calling function and passing only one argument   
except:  
  print( "Function needs two positional arguments" )  
  
  
  
########################################################################################################################
 
##function returning value or not returning ay value
#returning any value  
def square( num ):  
 return num**2     
print( "With return statement:",square( 39 ) ) # Calling function and passing arguments. 
#not returning any value  
def square( num ):  
 num**2   
print( "Without return statement:",square( 39 ) )# Calling function and passing arguments.



###################################################################################################################################################

##python_tutorial Function within Another Function(Nested function)
def function1():  
  string = 'python_tutorial functions tutorial'         
  def function2():  
    print( string )  
  function2()  
function1()

#############################################################################################################################################################################
##lambda function(function having no name & no return value)
def reciprocal( num ):  #normal function definition
  return 1 / num  
lambda_reciprocal = lambda num: 1 / num #lambda function definition 
print( "Def keyword: ", reciprocal(6) ) #calling using the function defined by def keyword  
print( "Lambda keyword: ", lambda_reciprocal(6) ) #calling using the function defined by lambda keyword   

#using/defining lambda function as an return statement in function
def myfunc(n):
  return lambda a:a*n #define lambda function
mydoubler=myfunc(2)
mytripler=myfunc(3)
print(mydoubler(11))
print(mytripler(12))



##Using Lambda Function with specific function(so that it can operate on iterable)
#Using Lambda Function with filter()
#Here's a simple illustration of using the filter() method to return only odd numbers from a list.
list_ = [34, 12, 64, 55, 75, 13, 63]    
odd_list = list(filter( lambda num: (num % 2 != 0) , list_ ))  #here filter takes lambda function & list to filter It & produce output (lambda function operate on/ takes on list(iterable) & produce function result)  
print(odd_list)

#Using Lambda Function with map()
#The map() method is used to cube  all the entries in a list in this example.
numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]    
cube_list = list(map( lambda num: num ** 3 , numbers_list ))  #here map() takes lambda function & list to map It & produce output (lambda function operate on/ takes on list(iterable) & produce function result)   
print( cube_list )  



#Using Lambda Function with List Comprehension
#Code to calculate square of each number of list using list comprehension 
l1=[1,2,3,4,5]
squares_list = [lambda num = num: num ** 2 for num in l1 if num !=2]
print("squared_list:",squares_list)
for square in squares_list:  
  print( square(), end = " ")
  
  
#transpose of matrix using list comprehension
matrix=[[1,2],[3,4],[5,6],[7,8]]
transpose=[[row[i] for row in matrix] for i in range(2)] #first (for i in range(2)) is executed/evaluted then for each 'for i in range(2)' the [row[i] for row in matrix] is evaluated & executed(creating list inside list here by using'[row[i] for row in matrix]')
print("\ntranspose:",transpose)

  
  
#Using Lambda Function with if-else
#Code to use lambda function with if-else  
Minimum = lambda x, y : x if (x < y) else y  
print(Minimum( 35, 74 ))  
  
  
#Using Lambda with Multiple Statements(used also with higher order function which takes one or more function as an aruments an return one or more function)
higher_ord_func=lambda x,func:x+func(x) # 'x+func(x)' is same as 'x+lambda x:x*x'
print("higher_ord_func:",higher_ord_func(20,lambda x:x*x))


#########################################################################################################################

#Recursion in python_tutorial(function calling itself)
#Example 1: A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8…
# Program to print the fibonacci series upto n_terms
def recursive_fibonacci(n):
 if n <= 1:
  return n
 else:
  return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
n_terms = 10
# check if the number of terms is valid
if n_terms <= 0:
 print("Invalid input ! Please input a positive value")
else:
 print("Fibonacci series:")
for i in range(n_terms):
 print(recursive_fibonacci(i))




###############################################################################################################################################


#Assigning function as an variable
#Example1
def func1(msg):     
  print(msg)  
func1("Hii")  
func2 = func1 #assigning fun1 to func2
func2("Hiii") 

#inner function
def func():  
 print("We are in first function")  
 def func1():  
  print("This is first child function of func")  
 def func2(): 
  print("This is second child function of func")  
 func1()  
 func2()  
func()  



#function returning function
def hello():  
 def hi():  
  print("Hello")  
 return hi  #returning 'hi()/hi' as function return
hello() #no refernce variable to take return value(which is function) 
new=hello() #assigning hi(return value of hello() to new now: new=hi 
new() #calling hi()

#Decorator example_1
def add(x):  
 return x+1  
def sub(x):  
 return x-1  
def operator(func, x):  #here 'operetor()' is generator which modify the behaviour of add()/sub() since it is passed as an argumen
 print("func:",func.__name__)
 temp = func(x)      #retuning x+1/x-1 as return value to 'temp'
 return temp  
print(operator(sub,10))  
print(operator(add,20))
 

#Decorator example_2
#function_in_python_tutorial.py
from Debugly import debug

@debug                      #here each function is decorated but hides implementation detail
def add(x,y): 
  return x+y

@debug
def sub(x,y):
  return x-y

@debug
def mul(x,y):
  return x*y

@debug
def div(x,y):
  return x/y





 
#####################################################################################################################################
#module in python_tutorial( a simple module, calc.py)
"""
def add(x, y):
	return (x+y)         #this code/module is available in 'calc.py' & can be imported in this file 'functions.py' & can be imported using the 'import'
def subtract(x, y):
  return (x-y)
  
"""
#importing module calc.py
import PYTHON.python_tutorial.Module as Module#importing module 'calc.py'
print(Module.add(10, 2))


#Importing specific attributes from the module
#Here, we are importing specific sqrt and factorial attributes from the math module.
from math import sqrt, factorial #in case importing all function we use '*'
print(sqrt(16))# if we simply do "import math", then 'math.sqrt(16)' and 'math.factorial()' are required.
print(factorial(6))

#Directories List for Modules
# importing sys module
import sys
# importing sys.path
print(sys.path)



#Renaming the python_tutorial module
# importing sqrt() and factorial from the
# module math
import math as mt
print(mt.sqrt(16))
print(mt.factorial(6))




#Example1
#Import Module from package
from python_tutorial import mod_1
from python_tutorial import mod_2
mod_1.gfg()
res = mod_2.sum(1, 2)
print(res)
#Example2
#Import Specific function from the module
from python_tutorial.mod_1 import gfg
from python_tutorial.mod_2 import sum
gfg()
res = sum(1, 2)
print(res)






# importing built-in module math
import math
# using square root(sqrt) function contained
# in math module
print(math.sqrt(25))
# using pi function contained in math module
print(math.pi)
# 2 radians = 114.59 degrees
print(math.degrees(2))
# 60 degrees = 1.04 radians
print(math.radians(60))
# Sine of 2 radians
print(math.sin(2))
# Cosine of 0.5 radians
print(math.cos(0.5))
# Tangent of 0.23 radians
print(math.tan(0.23))
# 1 * 2 * 3 * 4 = 24
print(math.factorial(4))
# importing built in module random
import random
# printing random integer between 0 and 5
print(random.randint(0, 5))
# print random floating point number between 0 and 1
print(random.random())
# random number between 0 and 100
print(random.random() * 100)
List = [1, 4, True, 800, "python_tutorial", 27, "hello"]
# using choice function in random module for choosing a random element from a set such as a list
print(random.choice(List))


############################################################################################################################################
#Namespace in python_tutorial(Namespaces are used to store and organize python_tutorial objects, such as variables, functions, and classes. They help to avoid naming conflicts and make it easier to access and manage objects in a program.)
var1 = 5#var1 is in the local namespace
def some_func():
  var2 = 6#var2 is in the local namespace
  def some_inner_func():
   var3=7#var3 is in the nested local namespace





 


       




  
 

  



 