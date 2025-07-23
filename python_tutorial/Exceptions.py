###########################################EXCEPTION HANDLING IN PYTHON#################################################
###########################################CONCEPTS OF MULTITHREADING & MULTIPROCESSING IN PYTHON#############################################
##ERROR IN PYTHON
'''
#1.Syntax Error(When the proper syntax of the language is not followed then a syntax error is thrown. Syntax errors is causes by the programmer.)
amount = 10000
if(amount>2999) # syntax error(here ':' is missing so syntax error occur)
 print("You are eligible to purchase Dsa Self Paced")
'''



'''
#2.Runtime Error/Exceptions(Some unwanted & unexpected  event that causes disturbance in normal-flow/execution of a program is called exceptions)
marks = 10000
# perform division with 0
a = marks / 0  #exception occurs here(ZeroDivisionError: division by zero error)
print(a)
'''
#####################################################################################################################################################################################
#Types of Exception in Python
#1.Predefined exception(exception  automatically raised by PVM based on  some  unwanted event  occur&  it creates object of that  exception class)like ZeroDivisionError, ValueError etc
#2.User defined exception(exception define &raised by programmer explicitely to meets its requirement(to indicate somethin g goes wrong by using 'raise' keyword).PVM have no ideas about these exception like UnsuffucientAmountError, TooOldError,TooYoungException, InvalidPinError  etc..
#Example: User defined exception[How to define & raise customised exception[To raised customised exception we should have to define a class which is derived class of BaseException class]
class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg=msg

class TooOldException(Exception):
    def __init__(self,msg):
        self.msg=msg
        
age= int(input("enter your age"))
if age>60:
    raise TooOldException("you are too old to get married")
elif age<18:
   raise TooYoungException("you are too young to married")
else:
   print("defined not details")



############################################################################################################################################################################################################
#Python Exception Hierarchy
'''
Sr.No.	Name of the Exception	Description of the Exception
1	Exception	All exceptions of Python have a base class.
2	StopIteration	If the next() method returns null for an iterator, this exception is raised.
3	SystemExit	The sys.exit() procedure raises this value.
4	StandardError	Excluding the StopIteration and SystemExit, this is the base class for all Python built-in exceptions.
5	ArithmeticError	All mathematical computation errors belong to this base class.
6	OverflowError	This exception is raised when a computation surpasses the numeric data type's maximum limit.
7	FloatingPointError	If a floating-point operation fails, this exception is raised.
8	ZeroDivisionError	For all numeric data types, its value is raised whenever a number is attempted to be divided by zero.
9	AssertionError	If the Assert statement fails, this exception is raised.
10	AttributeError	This exception is raised if a variable reference or assigning a value fails.
11	EOFError	When the endpoint of the file is approached, and the interpreter didn't get any input value by raw_input() or input() functions, this exception is raised.
12	ImportError	This exception is raised if using the import keyword to import a module fails.
13	KeyboardInterrupt	If the user interrupts the execution of a program, generally by hitting Ctrl+C, this exception is raised.
14	LookupError	LookupErrorBase is the base class for all search errors.
15	IndexError	This exception is raised when the index attempted to be accessed is not found.
16	KeyError	When the given key is not found in the dictionary to be found in, this exception is raised.
17	NameError	This exception is raised when a variable isn't located in either local or global namespace.
18	UnboundLocalError	This exception is raised when we try to access a local variable inside a function, and the variable has not been assigned any value.
19	EnvironmentError	All exceptions that arise beyond the Python environment have this base class.
20	IOError	If an input or output action fails, like when using the print command or the open() function to access a file that does not exist, this exception is raised.
22	SyntaxError	This exception is raised whenever a syntax error occurs in our program.
23	IndentationError	This exception was raised when we made an improper indentation.
24	SystemExit	This exception is raised when the sys.exit() method is used to terminate the Python interpreter. The parser exits if the situation is not addressed within the code.
25	TypeError	This exception is raised whenever a data type-incompatible action or function is tried to be executed.
26	ValueError	This exception is raised if the parameters for a built-in method for a particular data type are of the correct type but have been given the wrong values.
27	RuntimeError	This exception is raised when an error that occurred during the program's execution cannot be classified.
28	NotImplementedError	If an abstract function that the user must define in an inherited class is not defined, this exception is raised.
'''


#########################################################################################################################################################################################################################
'''
#Example_1.1: Python code to catch an exception and handle it using try and except code blocks  
a = ["Python", "Exceptions", "try and except"]  
try:  
 #looping through the elements of the array a, choosing a range that goes beyond the length of the array  
 for i in range( 4 ):  #Here exception occurs
  print( "The index and element from the array is", i, a[i] )  
  #if an error occurs in the try block, then except block will be executed by the Python interpreter (PVM)      
except:  
 print ("Index out of range") 
 '''
 
 

#Example1.2:to print exception on the console
try:
  print(10/0)
except ZeroDivisionError as msg:     # here we can use the 'BaseException'  class as it can handle all its derived exceptions
  print("exception type",type(msg))
  print("exception type",msg.__class__)
  print("exception class name",msg.__class__.__name__)
  print("exception message",msg)


'''
#Example_1.3:Try with multiple except block(order to handle multiple exceptions depending upon exception type occurs)
try:
  print(10/0)
except (Arithematic Error):
  print("arithematic error occurs")  #In above code although there is ZeroDivisionError occurs but and 'print("zero division error")' should be printed but PVM will print("arithematic error  occurs") as ArithematicError is Base class of ZeroDivisionError
except ZeroDivisionError:
  print("zero division error")
'''

#Example_1.4:single except block handling multiple exception
try:
 x=int(input("enter value of x"))
 y=int(input("enter value of y"))
 z=x/y
except(ZeroDivisionError, ValueError) as msg:  # here multiple exception is  forming tuple & any exception occurs it matches its type, bind it with its class & throw its object
 print("the raised exceptions:", msg.__class__)
 print("exception message:",msg)
  


#Example_1.5:Default Except block(We use default except block to handle any type of exception & generally used to print exception information to console. It must be defined as last except block otherwise syntax error will occurs)
try:
   a=int(input("enter value of a"))
   b=int(input("enter value of b"))
   z=a/b
except (ZeroDivisionError) as msg:  # here multiple exception is  forming tuple
  print("exception message",msg)
except ValueError as msg:
  print("exception message:",msg)  
except:
  print("default exception occurs")
  
######################################################################################################################################################################################################################################################################  
'''
#Example_2.1: 'try-except-final' block[Case1: Exception raised but not handled with proper exception ]
try:
  print("try")
  print(10/0)
except ValueError as msg:
  print("error is:",msg)
finally:
  print("finally bock executed") #this block is always executed whether exception occurs or not(it is used for resource clean-up for try block)
'''
 
 
#Example_2.2: 'try-except-final' block[Case2: Exception raised & handled with proper exception object]
try:
  print("try")
  print(10/0)
except ZeroDivisionError as msg:
  print("error is:",msg)
finally:
  print("finally bock executed") #this block is always executed whether exception occurs or not(it is used for resource clean-up for try block)


 
#Example_2.3:Finally block VS  os.exit(0)[There is one situation where finally block did not get executed & that is when we explicitely down the PVM by calling the os._exit(0) so that further part of program did not get executed]
import os
try:
  print("try block")
  #print(5/0) # if its executed then finally block also get executed
  os._exit(0)#--'0' normal terminatiom/status code/ there is no effect if there is non zero status code or not PVM take its as internally
except ValueError:
  print("value error occurred")
finally:
  print("finally block get executed")  #not executed at this moment
  


##Else with try-except-finally block-It will be executed if there is no exception in try block. there is no chance to execute 'except'& 'try' block simultaneously and whenever we are using the else block then we must have to use except block but vice-versa is not true
#Example_2.4.1:Else with try-except-finally block
#Python code to illustrate working of try() 
def divide(x, y): 
  try: 
   result = x // y #Floor Division : Gives only Fractional Part as Answer 
  except ZeroDivisionError: 
   print("Sorry ! You are dividing by zero ") 
  else:
   print("Yeah ! Your answer is :", result) 
  finally:
   print("finally block gets executed")
#Look at parameters and note the working of Program 
divide(3, 2) # here 'else' block will be executed as there is no exception occurs in try block(3//2)
divide(3, 0) # here 'else' block will not be executed as there is an exception occurs in try block(3//0)





#Example_2.4.2:Else with try-except-finally block
#Else with try-except-finally block using for loop with 'break'
try:
    for i in range(10):
        if i == 5:
            break #
        print(i)
except Exception as e:
    print(e)
else:
    print("No exceptions occurred.") # here 'else' block will not be executed as there is no exception occurs in try block although there is 'break' in for loop(since it is not in 'for-else' combination so that's the reason behind it(ValueError as i==5 for i=5)
finally:
    print("This will always be executed.")
 
 
 
 
#Example_2.4.3:Else with try-except-finally block
try:
  print("try")
  filepointer=open("abc.txt","r")
except:
  print("file not found error")
else:
  print("file opend successfully")   # here 'else' block will  not be executed as there is an exception occurs in try block('FileNotFoundError' as there is no file name 'abc.txt')
  print(filepointer.read())
finally:
  print("file gets closed if its opened aleady")
  #filepointer.close()
  
 
 
 
  
#Example_2.4.4:Else with try-except-finally block  using for loop 
for x in range(100):
    if x>10:
     break
     print("the current item is", x)
else: 
    print("all item processed successfully")  # here 'else' did not get executed because there is 'break' in for loop
    
###############################################################################################################################################################################################################################################################################
'''
#Control flow in nested try- except-finally blocks
Try:
      stmt1
      stmt2
      stmt3
      try:  
          stmt4
          stmt5
          stmt6
      except:
          stmt7
     finally:
          stmt8
     stmt9
Except:
   stmt10
Finally:
   stmt11
Stmt12   #this will be execute when outer except is executed otherwise not

Case1:if there is no exception
       stmt1-stmt2-stmt3-stmt4-stmt5-stmt6-stmt8-stmt9-stmt11-stmt12-normal termination
Case2:if there is  exception at stmt2 and corresponding handling code available(outer except block)
       stmt1-stmt10-stmt11-stmt12-normal termination
Case3:if there is  exception at stmt2 and corresponding handling code  not available(outer except block)
       stmt1-stmt11-abnormal termination
Case4:if there is  exception at stmt5 and corresponding handling code available(inner except block)
       stmt1-stmt2-stmt3-stmt4-stmt7-stmt8-stmt9-stmt11-stmt12-normal termination
Case5:if there is  exception at stmt5 and corresponding handling code not available(inner except block) but (outer except block available)
       stmt1-stmt2-stmt3-stmt4-stmt8-stmt10-stmt11-stmt12-abnormal termination
Case6:if there is  exception at stmt5 and corresponding handling code available(inner except block)
       stmt1-stmt2-stmt3-stmt4-stmt11-stmt12-normal termination
Case7:if there is  exception at stmt7 and corresponding handling code  available(outer except block)
        stmt1-stmt2-stmt3-*-*-*stmt8-stmt11-stmt12-normal termination
Case8:if there is  exception at stmt7 and corresponding handling code not  available(outer except block)
        stmt1-stmt2-stmt3-*-*-*stmt8-stmt11-abnormal termination
Case9:if there is  exception at stmt8 and corresponding handling code available(outer except block)
         stmt1-stmt2-stmt3-*-*-*-*-stmt8-stmt10-stmt11-stmr12-normal termination
Case9:if there is  exception at stmt8 and corresponding handling code not available(outer except block)
          stmt1-stmt2-stmt3-*-*-*-*-stmt8-stmt10-stmt11-stmr12-normal termination
Case10:if there is  exception at stmt8 and corresponding handling code not available(outer except block)
          stmt1-stmt2-stmt3-*-*-*-*-stmt11-normal termination
Case10:if there is  exception at stmt9 and corresponding handling code available(outer except block)
           stmt1-stmt2-stmt3-*-*-*-*stmt8-stmt10-stmt11-stmt12-normal termination(if stmt9 executed then stmt8 must be executed)
Case10:if there is  exception at stmt9 and corresponding handling  code  not available(outer except block)
           stmt1-stmt2-stmt3-*-*-*-*stmt8--stmt11--abnormal termination(if stmt9 executed then stmt8 must be executed)
Case10:if there is  exception at stmt10& stmt11-stmt12 then abnormal termination wiil occurs always

'''
