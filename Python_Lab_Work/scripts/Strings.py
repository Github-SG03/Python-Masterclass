########python program for string formating/Practise ################
print("hello world")# python string are immutable i.e: we can change shivam to shivan by str[5]= 'n' ,we can replaced it by a new string like  str="shivan"

print("hello \world")# here there is no meaning of \w so print as it is

print("hello\nworld")

print("They said,\tHello what's going on?")# horizontal tab
print("""They said,"Hello what's going on?""")
#the below print will cause SyntaxError so above is right print statement
#print("They said,"Hello what's going on?") 

print("Hello\vWorld!")

print("Python1 \
Python2 \
Python3") #\newline(ignores the newline)

str3 = """Triple quotes are generally used for  
represent the multiline or 
     docstring"""   
print(str3)  

print("Hello\fWorld!")

print("\"")
print(r"\"")#\"

print("\a")#audio bell

print("Hello\rWorld!")# carriage return

print("\x48\x65\x6c\x6c\x6f")#Hello

print("\110\145\154\154\157")#Hello(octal representation)
print(r"\110\145\154\154\157")#\110\145\154\154\157
                              #r"---------" is used in the case of escape sequence occurs in the string(\) followed by any character having meaning togethet with it 


print("C:\\Users\\shivam\\Python3.10\\Lib")
print(r"C:\\Users\\shivam\\Python3.10\\Lib") 



##string formating using 'format()'
# Using Curly braces  
print("{} and {} both are the best friend".format("Devansh","Abhishek"))    
#Positional Argument  
print("{1} and {0} best players ".format("Virat","Rohit"))    
#Keyword Argument  
print("{a},{b},{c}".format(a = "James", b = "Peter", c = "Ricky"))  

#string indexing & slicing
str = "JAVATPOINT"  
# Start Oth index to end  
print(str[0:])  
# Starts 1th index to 4th index  
print(str[1:5])  
# Starts 2nd index to 3rd index  
print(str[2:4])  
# Starts 0th to 2nd index  
print(str[:3])  
#Starts 4th to 6th index  
print(str[4:7])

#in reverse order
str = 'TUTORIALPOINT'  
print(str[-1])  
print(str[-3])  
print(str[-2:])  
print(str[-4:-1])  
print(str[-7:-2])  
# Reversing the given string  
print(str[::-1])  

#deleting the string
str1 = "JAVATPOINT"  
del str1  #can't do (del str1[5]) 
#print(str1)

##string operator
#another example1 
str = "Hello"     
str1 = " world"    
print(str*3) # prints HelloHelloHello    
print(str+str1)# prints Hello world     
print(str[4]) # prints o                
print(str[2:4]); # prints ll                    
print('w' in str) # prints false as w is not present in str    
print('wo' not in str1) # prints false as wo is present in str1.     
print(r'C://python37') # prints C://python37 as it is written    
print("The string str : %s"%(str)) # prints The string str : Hello

#another example2   
Integer = 10    
Float = 1.290    
String = "meEruT" 
string="simmi"   
print("Hi I am Integer ... My value is %d\nHi I am float ... My value is %f\nHi I am string ... My value is %s"%(Integer,Float,String)) 


#string built-in function 
print(String.upper())#converts 'meEruT' to 'MEERUT'
print(String.title())##converts 'meEruT' to 'Meerut'
print(String.swapcase())#converts 'meEruT' to 'MEeRUT'
print(len(String))# gives length of string
print(String.isupper())
print(String.isspace())# returms True if string have " "
print(String.isnumeric())# returms true if string contains only numeric charater
print(String.isdigit())#It returns true if all the characters are digits and there is at least one character, otherwise False.
print("shivam is {} hard for examinatiom".format("working"))
print(String.capitalize)
print(String.isalpha)
print(String.isalnum)
print(String.isprintable())
print(String.isprintable())
print(String.isidentifier())
print(String.isascii)
print(String.isnumeric())
print(String.index("sim"))
print(String.count('e',0,5)) # 1 occurence of 'e' in 'meEruT'
print(string.find('m',0,5))# 2nd location occurence of 'm' in 'simmi'
print(string.endswith('i',0,2))
print(String.startswith('s',0,2))
print(String.strip())
print(String.lstrip())
print(String.ljust("&"))
print(String.center("$"))
print(String.casefold())
print(String.encode())
print(String.removesuffix())
print(String.splitlines())
print(String.expandtabs())
print(String.translate(string))
print(String.replace(String,"DeElhi"))
print("-".join("shivam"))
print(String.partition("l"))
print(String.split("E"))
print(String.isdecimal())
print(String.__sizeof__())
print(String.__doc__())

 















