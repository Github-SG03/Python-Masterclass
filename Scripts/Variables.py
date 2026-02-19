####python program for variable understanding#######
#string1
name="shivam"

#string2
gender='M'

#integer
roll_number=88

#floating_number
percentage_obtained=95.6
percentage_obtained_previous=94.6

#boolean
is_male=True

#print the values
print(name,roll_number,percentage_obtained,is_male)

#print the values type
print(type(name))

#print the values of roll_number in character
print(chr(roll_number))
#print the values of gender in ASCII
print(ord(gender))

#give & print feedback response for Shivam's performance through 'input()' function
feedback=input("enter your feedback:")
print(feedback)
#using typecasting for feedback number
feedback_number=int(input("enter your feedback number from 1-10:"))
print(feedback_number)

#print the student detail in 1 line
print("my name is",name,"my roll_numer is",roll_number," & i got percentage in exam",percentage_obtained)

#print the student detail in 1 line using expression
print("my previous exam percentage was",percentage_obtained-1.0)

#print the student detail values in 1 line using separator
print(name,roll_number,percentage_obtained,is_male,sep="@")

#'separator' with 'end' in student detail
print("name =", name, sep='#',end='\n')

#object/variable identity
a = 50  
b = a  
print(id(a))  
print(id(b))  
# Reassigned variable a  
a = 500  
print(id(a))
print(id(b))

#assigning same values to multiple variable
x=y=z=50     
print(x)    
print(y)    
print(z)

#assigning multiple value to multiple variable
x,y,z=5,10,15
print(x)    
print(y)    
print(float(z)) 


#'eval()' function
a=eval(input("enter any binary number:"))
b=eval(input("enter any decimal number:"))
print("a+b:",a+b)


"""
#deleting a variable
m=23
del m
print(m)
"""


##local & global variable
#local variable
def add():  
 a = 20 # local varible(scope within function)
 b = 30 # local varible(scope within function)
 c = a + b #local varible(scope within function) 
 print("The sum is:", c) 
add()
#print(a)  NameEror 



#global variable
x = 101 # Global variable in function  
def mainFunction():  
 global x  
 print(x) # printing a global variable   
 # modifying a global variable  
 x = 'Welcome To Javatpoint'  
 print(x)  
    
mainFunction()  
print(x) 

# A Python program to display that we can store large numbers in Python(it does not have specific datatype to store such large number such as long,short etc)     
a = 10000000000000000000000000000000000000000000  
a = a + 1  
print(type(a))  
print ((a))  #same as print(a)


