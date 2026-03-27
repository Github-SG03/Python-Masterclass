#############################Python program for is statement################################################
def _read_int(prompt, default=0):
    try:
        return int(input(prompt))
    except EOFError:
        return default
    except ValueError:
        return default

#if statement(to check one condition)
num = _read_int("enter the number?")  
if num%2 == 0:  
    print("Number is even")  
 
    
#if-else statement(to check two condition)
num = _read_int("enter the number?")  
if num%2 == 0:  
 print("Number is even...")  
else:  
  print("Number is odd...") 
  
  
#nested if statement(to check condition under another condition) 
num = 15
if num >= 0: 
	if num == 0: #if statemet inside if
		print("Zero") 
	else: 
		print("Positive number") 
else: 
	print("Negative number") 
 
 
# multiple if-ladder(multiple if statement-to check multiple condition)
a = _read_int("Enter a? ")  
b = _read_int("Enter b? ") 
c = _read_int("Enter c? ")  
if a>b and a>c:  
 print("a is largest")  
if b>a and b>c:  
 print("b is largest") 
if c>a and c>b:  
 print("c is largest") 
 
 
#if-else ladder(multiple if statement-to check multiple condition)/improved form of multiple if-ladder
marks = _read_int("Enter the marks? ")  
if marks > 85 and marks <= 100:  
  print("Congrats ! you scored grade A ...")  
elif marks > 60 and marks <= 85:  
  print("You scored grade B + ...")  
elif marks > 40 and marks <= 60:  
  print("You scored grade B ...")  
elif (marks > 30 and marks <= 40):  
  print("You scored grade C ...")  
else:  
  print("Sorry you are fail ?")
  
  
  
  
