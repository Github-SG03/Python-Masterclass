#defining function to return list of fibonacci elements

def fibonacci(n):
    
    l = [0,1] 
    for i in range(2,n):
        l.append(l[-1]+l[-2])
    return l

#Main function
if __name__ == "__main__":
   #defining the total number of elements
    n = 10
    
    #calling of function
    fibo = fibonacci(n)
    
    #displaying the function  
    print("Fibonacci Series: ",*fibo)