############################################python program for for_loop##############################
#Example1
# Code to find the sum of squares of each element of the list using for loop    
# creating the list of numbers  
numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]     
# initializing a variable that will store the sum  
sum_ = 0     
# using for loop to iterate over the list  
for i in numbers:        
 sum_ = sum_ + i ** 2      
 print("The sum of squares is: ", sum_)  
 
 
 #Example2/using range()
my_list = [3, 5, 6, 8, 4]  
for iter_var in range( len( my_list ) ):  
  my_list.append(my_list[iter_var] + 2)  
print( my_list )  
 
 
#Example3.1
#printing the character of string "welcome to wscubetech"
w="welcome to wscubetech"
t=len(w)
for i in range(t):#t having 21 length so range will be 0-21
    print(w[i])
    
#Example3.2
#printing the character of string "welcome to wscubetech"
w="welcome to wscubetech"
t=len(w)
for i in w:#t having 21 length so range will be 0-21
    print(i)
#Example3.3
#printing the reverse character of string "welcome to wscubetech" using slicing
w="welcome to wscubetech"
w=w[::-1]
t=len(w)
for i in w:#t having 21 length so range will be 0-21
    print(i)
 
 
    
#Example4.1
#printing the character of string "welcome to wscubetech" using slicing   
w="welcome to wscubetech"
w=w[::-1]#reverse the string
t=len(w)
for i in range(t):#t having 21 length so range will be 0-21
    print(w[i])   
#Example4.2
#printing the character of string "welcome to wscubetech" using negative range
w="welcome to wscubetech"
t=len(w)
for i in range(t-1,-1,-1):#t having 21 length so range will be 0-21
    print(w[i])
    
    
#using else statement in else-block(its execute else block if there is no break statement get executed)
#CODE_1:
for i in range(1, 4): 
	print(i) 
else: # Executed because no break in for 
	print("No Break") 
	
	
#CODE_2:
for i in range(1, 4): 
	print(i) 
	break
else: # Not executed as there is a break 
	print("No Break") 


	
#CODE_3:
# Python 3.x program to check if an array consists of even number 
def contains_even_number(l): 
	for ele in l: 
		if ele % 2 == 0: 
			print ("list contains an even number") 
			break

	# This else executes only if break is NEVER 
	# reached and loop terminated after all iterations. 
	else:	 
		print ("list does not contain an even number") 

# Driver code 
print ("For List 1:") 
contains_even_number([1, 9, 8]) 
print (" \nFor List 2:") 
contains_even_number([1, 3, 5]) 



#Example1.1
#nested for loop
x = [1, 2]
y = [4, 5]
for i in x:
 for j in y:
  print(i, j)


#Example1.2(program to print table of 2)
#nested for loop
# Running outer loop from 2 to 2
for i in range(2, 3):

	# Printing inside the outer loop
	# Running inner loop from 1 to 10
	for j in range(1, 11):

		# Printing inside the inner loop
		print(i, "*", j, "=", i*j)
	# Printing inside the outer loop
	print()
 
 
##loop control statement
#break() The break is a keyword in python which is used to bring the program control out of the loop & if placed inside nested for loop then control goes to next statement of outer for loop for execution 
str = "python"  
for i in str:  
 if i == 'o':  
  break  
 print(i) 
 
 
 
#continue() In Python, the continue keyword return control of the iteration to the beginning of the Python for loop & All remaining lines in the prevailing iteration of the loop are skipped by the continue keyword, which returns execution to the beginning of the next iteration of the loop.
#Python code to show example of continue statement looping from 10 to 20  
for iterator in range(10, 21):  
# If iterator is equals to 15, loop will continue to the next iteration  
 if iterator == 15:  
   continue  
 #otherwise printing the value of iterator  
 print( iterator )   
 
 
 
#pass() We can use the pass statement as a placeholder when unsure what code to provide. So, we only have to place the pass on that line. Pass may be used when we don't wish any code to be executed.
# Python program to show how to use a pass statement in a for loop  
'''''pass acts as a placeholder. We can fill this place later on'''  
sequence = {"Python", "Pass", "Statement", "Placeholder"}  
for value in sequence:  
    if value == "Pass":  
        pass # leaving an empty if block using the pass keyword  
    else:  
        print("Not reached pass keyword: ", value)  
        

  
   

    
