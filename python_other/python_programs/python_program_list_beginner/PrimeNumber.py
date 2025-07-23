#############################LIST OF PYTHON PROGRAM'S####################################################

#PROGRAM_1:TO CHECK WHETHER A NUMBER IS PRIME OR NOT
n=int(input("Enter a number to check whether it is prime number or not:"))
if n<=1:
    print("it is not a prime number")
else:
    is_prime=True  #flag variable for holding prime number
    for i in range(2,n):  # to check validity for number having factor between 2 to n-1 as[2,3,4,5,6...n-1] since the number having factor 1 & itself is considered to be prime number otherwise not.
        if n%i==0:        # for better performance we can take also range(2, n//2+1) it means if half of iteration does not satisfy the condition for prime number like( for n=23: we can check upto n//2+1 which is 12 so we have to check validy between 2 to n//2=1 or 2 to 12)
            is_prime=False
            break
    if is_prime==True:
        print("it is prime number")
    else:
        print("it is not a prime number")
        


#PROGRAM_2:TO GENERATE PRIME NUMBER WHICH ARE LESS THAN OR EQUAL TO N
n=int(input("Enter a number to check whether it is prime number or not:"))
n1=2
while n1<=n:
    #code to check n1 is prime or not
    is_prime=True
    for i in range(2,n1):
        if n1%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(n1)
    n1=n1+1
    
    
    

        
        
        