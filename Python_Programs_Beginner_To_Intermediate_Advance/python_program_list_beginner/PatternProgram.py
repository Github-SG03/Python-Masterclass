#############################################################PATTERN_PROGRAM'S IN PYTHON########################################################################################################################
#EXAMPLE_2: TO PRINT PATTERN WITH * SYMBOL
"""
* * *
"""
n=int(input("enter number of row:"))
for i in range(n):     #loop will be executed 3 times
    print("*",end=' ')
print("\n")
    
    
  
    
#EXAMPLE_2: TO PRINT SQUARE PATTERN WITH * SYMBOL
"""
* * * 
* * * 
* * * 
"""
n=int(input("enter number of rows:"))
for i in range(n):     #loop will be executed 3 times
    print("* "*n) 
    
    
    
    
#EXAMPLE_3: TO PRINT SQUARE PATTERN WITH PROVIDED FIXED DIGIT
"""
3 3 3 
3 3 3
3 3 3
"""  
n=int(input("enter number of rows:"))
for i in range(n):     #loop will be executed 3 times
    print((str(n)+' ')*n) 
    
    
    
 
#EXAMPLE_4: TO PRINT SQUARE PATTERN WITH PROVIDED FIXED DIGIT IN EVERY ROW
"""
1 1 1
2 2 2  
3 3 3
"""
n=int(input("enter number of rows:"))
for i in range(n):         #loop will be executed 3 times
    print((str(i+1)+' ')*n)# first time(for first row) i==0 , second time(for second row) i==1 & so on.....
    
    
    
    
#EXAMPLE_5: TO PRINT SQUARE PATTERN WITH FIXED ALPHABET SYMBOL
"""
A A A 
A A A 
A A A 
"""
n=int(input("enter number of rows:"))
for i in range(n):     #loop will be executed 3 times
    print("A "*n) 
    
    


#EXAMPLE_6: TO PRINT SQUARE PATTERN WITH ALPHABET SYMBOL
"""
A A A 
B B B
C C C
"""
n=int(input("enter number of rows:"))
for i in range(n):     #loop will be executed 3 times
    print((chr(65+i)+' ')*n) #  for first row:chr(65+i) ==chr(65+0)==A, for second row:chr(65+i)==chr(65+1)==B & so on.....
    
    
    
    
#EXAMPLE_7: TO PRINT SQUARE PATTERN WITH INCREASING DIGITS IN EACH COLUMN
"""
1 2 3
1 2 3
1 2 3

"""
n=int(input("enter number of rows:"))
for i in range(n): #loop will be executed 3 times
    for j in range(n):#loop will be executed 3 times for each value of i==0,1,2
        print(str(j+1),end=' ')
    print(" ")#blank space for each row
    
    
    
    
    
#EXAMPLE_8: TO PRINT SQUARE PATTERN WITH INCREASING ALPHABETS IN EACH COLUMN
"""
A B C
A B C
A B C
"""
n=int(input("enter number of rows:"))
for i in range(n):     #loop will be executed 3 times
    for j in range(n):
        print(chr(65+j),end=' ')#  for first row:chr(65+i) ==chr(65+0)==A, for second row:chr(65+i)==chr(65+1)==B & so on..... 
    print(" ")#blank space for each row       



    
#EXAMPLE_9: TO PRINT SQUARE PATTERN WITH PROVIDED NON-FIXED DIGIT IN EVERY ROW
"""
3 3 3
2 2 2
1 1 1
"""
n=int(input("enter number of rows:"))
for i in range(n):         #loop will be executed 3 times
    print((str(n-i)+' ')*n)#str(n-1) first time(for first row) i==0 is same as str(3-0)==str(3)==='3', second time(for second row) i==1 & so on.....

    
    
 
 
 
#EXAMPLE_10: TO PRINT SQUARE PATTERN WITH ALPHABET SYMBOL IN REVERSE ORDER
"""
C C C
B B B
A A A
""" 
n=int(input("enter number of rows:"))
for i in range(n):     #loop will be executed 3 times
    print((chr(64+n-i)+' ')*n) #  for first row:chr(64+n-i) ==chr(65+0)==A, for second row:chr(65+i)==chr(65+1)==B & so on.....







#EXAMPLE_11: TO PRINT SQUARE PATTERN WITH DIGITS IN DECREASING ORDER IN EVERY COLUMN
"""
3 2 1
3 2 1
3 2 1
"""
n=int(input("enter number of rows:"))
for i in range(n): #loop will be executed 3 times
    for j in range(n):#loop will be executed 3 times for each value of i==0,1,2
        print(str(n-j),end=' ')
    print()#blank row after each row
    
    



#EXAMPLE_12: TO PRINT SQUARE PATTERN WITH ALPHABET SYMBOL IN REVERSE ORDER IN EACH COLUMN
"""
C B A
C B A
C B A
"""
n=int(input("enter number of rows:"))
for i in range(n):     #loop will be executed 3 times
    for j in range(n):
        print(chr(64+n-j),end=' ')#  for first row:chr(65+i) ==chr(65+0)==A, for second row:chr(65+i)==chr(65+1)==B & so on..... 
    print(" ")#blank space for each row   




#Example_13: TO PRINT RIGHT ANGLE TRIANGLE PATTERN WITH * SYMBOLS
"""
*
* *
* * *
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(i+1): # we have to only print value as respect to j
        print("*",end=' ')
    print()
    
    
    
 
 
 
    
#Example_13.1: TO PRINT RIGHT ANGLE TRIANGLE PATTERN WITH FIXED DIGIT IN EVERY ROW
"""
1
2 2
3 3 3
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(i+1): # we have to only print value as respect to j
        print(i+1,end=' ')
    print()
#Example_13.2: TO PRINT RIGHT ANGLE TRIANGLE PATTERN WITH FIXED DIGIT IN EVERY ROW WITHOUT NESTED FOR LOOP
"""
1
2 2
3 3 3
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print((str(i+1)+' ')*(i+1))

    
    
    
    
 
    
#Example_14.1: TO PRINT RIGHT ANGLE TRIANGLE PATTERN WITH FIXED ALPHABET IN EVERY ROW
"""
A
B B 
C C C
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(i+1): # we have to only print value as respect to j
        print(chr(65+i),end=' ')
    print()   
#Example_14.2: TO PRINT RIGHT ANGLE TRIANGLE PATTERN WITH FIXED ALPHABET IN EVERY ROW WITHOUT NESTED LOOP
"""
A
B B 
C C C
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print((chr(65+i)+' ')*(i+1))
    
    
    
    
    
#Example_15: TO PRINT RIGHT ANGLE TRIANGLE PATTERN WITH DIGITS IN  ASCENDING ORDER IN EVERY ROW
"""
1
1 2
1 2 3
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(i+1): # we have to only print value as respect to j
        print(str(j+1),end=' ')
    print()






#Example_16: TO PRINT RIGHT ANGLE TRIANGLE PATTERN WITH  INCREASING ALPHABET IN EVERY COLUMN
"""
A 
A B
A B C
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(i+1): # we have to only print value as respect to j
        print(chr(65+j),end=' ')
    print()  
    



#Example_17: TO PRINT RIGHT ANGLE TRIANGLE PATTERN WITH  DIGITS IN DECREASING ORDER IN EVERY ROW
"""
3
3 2
3 2 1
""" 
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(i+1): # we have to only print value as respect to j
        print(str(n-j),end=' ')
    print()
    
    
    
    
    
    
#Example_18:TO PRINT RIGHT ANGLE TRIANGLE PATTERN WITH ALPHABET SYMBOL IN REVERSE ORDER IN EVERY ROW
"""
C
C B
C B A
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(i+1): # we have to only print value as respect to j
        print(chr(64+n-j),end=' ')
    print()
    
    
    
    
    
    
#Example_18.1:TO PRINT  REVERSE RIGHT ANGLE TRIANGLE PATTERN WITH SYMBOL
"""
* * *
* *
*
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(n-i): # we have to only print value as respect to j
        print("*",end=' ')
    print()
#Example_18.2:TO PRINT  REVERSE RIGHT ANGLE TRIANGLE PATTERN WITH SYMBOL WITHOUT NESRED FOR LOOP
"""
* * *
* *
*
"""
for i in range(n):#loop will be executed  for 3 times/rows
    print("* "*(n-i))





#Example_19.1: TO PRINT RIGHT ANGLE TRIANGLE PATTERN WITH FIXED DIGITS EVERY ROW
"""
1 1 1
2 2
3
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(n-i): # we have to only print value as respect to j
        print(str(i+1),end=' ')
    print()     
#Example_19.2: TO PRINT RIGHT ANGLE TRIANGLE PATTERN WITH FIXED DIGITS EVERY ROW WITHOUT NESTED LOOP
"""
1 1 1
2 2
3
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print((str(i+1)+' ')*(n-i))
    
    
    
    
    
    
#Example_20.1: TO PRINT INVERTED RIGHT ANGLE TRIANGLE PATTERN WITH FIXED ALPHABET IN EVERY ROW 
"""
A A A
B B
C
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(n-i): # we have to only print value as respect to j
        print(chr(65+i),end=' ')
    print() 
#Example_20.2: TO PRINT INVERTED RIGHT ANGLE TRIANGLE PATTERN WITH FIXED ALPHABET IN EVERY ROW 
"""
A A A
B B
C
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print((chr(65+i)+' ')*(n-i))
    
    
    
    
    
    
    
#Example_21: TO PRINT INVERTED RIGHT ANGLE TRIANGLE PATTERN WITH FIXED DIGITS IN EVERY ROW 
"""
3 3 3
2 2
1
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(n-i): # we have to only print value as respect to j
        print(str(n-i),end=' ')
    print() 
    
    
    
    



#Example_22: TO PRINT INVERTED RIGHT ANGLE TRIANGLE PATTERN WITH FIXED ALPHABETS IN EVERY ROW 
"""
C C C
B B
A
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(n-i): # we have to only print value as respect to j
        print(chr(64+n-i),end=' ')
    print() 







#Example_23: TO PRINT INVERTED RIGHT ANGLE TRIANGLE PATTERN WITH DIGITS IN ASCENDING ORDER IN EVERY ROW 
"""
1 2 3
1 2
1
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(n-i): # we have to only print value as respect to j
        print(str(j+1),end=' ')
    print() 
    
    
    

#Example_24: TO PRINT INVERTED RIGHT ANGLE TRIANGLE PATTERN WITH ALPHABET SYMBOL IN INCREASING ORDER IN EVERY ROW 
"""
A B C
A B
A
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(n-i): # we have to only print value as respect to j
        print(chr(65+j),end=' ')
    print() 
    
    
    
    
    
    
#Example_25: TO PRINT INVERTED RIGHT ANGLE TRIANGLE PATTERN WITH DIGITS SYMBOL IN DESCENDING ORDER IN EVERY ROW 
"""
3 2 1(for j=0,1,2 & i=0)
3 2  (for j=0,1 & i=1)
3    (for j=0 & i=2)
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(n-i): # we have to only print value as respect to j
        print(str(n-j),end=' ')
    print() 
    
    
    
    
    
    
    
    
#Example_26: TO PRINT INVERTED RIGHT ANGLE TRIANGLE PATTERN WITH ALPHABETS SYMBOL IN DESCENDING ORDER IN EVERY ROW 
"""
C B A
C B
C
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    for j in range(n-i): # we have to only print value as respect to j
        print(chr(64+n-j),end=' ')
    print() 
    
    

    



#Example_27: TO PRINT PYRAMID PATTERN WITH '*' SYMBOL
"""
  *                    (2 spaces & 1's *) 
 * *                   (1 spaces & 2's *)                   [number of spaces in every row:n-i-1 & how many times '*' to printed in each row:i+1]
* * *                  ( no spaces & 3's *)
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print(' '*(n-i-1)+"* "*(i+1)) # printing the same element so nested for loop is not required
    
    
    
  
  
    
    
#Example_27: TO PRINT PYRAMID PATTERN WITH FIXED DIGIT IN EVERY ROW
"""
  1
 2 2
3 3 3
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))
    
    
    
    
    
    
#Example_28: TO PRINT PYRAMID PATTERN WITH FIXED ALPHABETS IN EVERY ROW
"""
  A
 B B
C C C
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print(' '*(n-i-1)+(chr(65+i)+' ')*(i+1))
    
    
    
    
    


#Example_29: TO PRINT PYRAMID PATTERN WITH DIGITS IN  ASCENDING ORDER IN EVERY ROW
"""
  1       (for j=0),print '1':after blank spaces gets printed
 1 2      (for j=0,1),print '1 2':after blank spaces gets printed                                   # here value is changing in columns of each row so we will take nested for loop
1 2 3     (for j=0,1,2),print '1 2 3':after blank spaces gets printed
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print(' '*(n-i-1),end=' ') #after printing space  for each row, cursor remains on same line for nested loop printing 
    for j in range(i+1):        #  here nested loop start working as soon as after outer loop printed the spaces
        print(j+1,end=' ')
    print()
    
    




#Example_30: TO PRINT PYRAMID PATTERN WITH ALPHABETS SYMBOLS IN ASCENDING ORDER IN EVERY ROW
"""
  A
 A B
A B C
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print(' '*(n-i-1),end=' ')
    for j in range(i+1):        #  here nested loop start working as soon as after outer loop printed the spaces
        print(chr(65+j),end=' ')
    print()
    
    
    
    
    
    
#Example_31: TO PRINT PYRAMID PATTERN WITH DIGITS SYMBOLS IN DESCENDING ORDER IN EVERY ROW
"""
  3
 3 2
3 2 1
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print(' '*(n-i-1),end=' ')
    for j in range(i+1):        #  here nested loop start working as soon as after outer loop printed the spaces
        print(str(n-j),end=' ')
    print()
    
    
    
    
    
    
    

#Example_32: TO PRINT PYRAMID PATTERN WITH ALPHABETS SYMBOLS IN DESCENDING ORDER IN EVERY ROW
"""
  C
 C B
C B A
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print(' '*(n-i-1),end=' ')
    for j in range(i+1):        #  here nested loop start working as soon as after outer loop printed the spaces
        print(chr(64+n-j),end=' ')
    print()
    
    
    
    
    




#Example_33: TO PRINT  INVERTED PYRAMID PATTERN WITH '*' SYMBOL
"""
* * *                  (no spaces & 3's) 
 * *                   (1 spaces & 2's *)                   [number of spaces in every row:i & how many times '*' to printed in each row:n-i]                
  *                    (2 spaces & 1's *)
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print(' '*(i)+"* "*(n-i)) # printing the same element so nested for loop is not required
    
    
    
    
    
    
      
   
#Example_34: TO PRINT  INVERTED PYRAMID PATTERN WITH FIXED DIGITS SYMBOL IN EVERY ROW
"""
1 1 1
 2 2
  3
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print(' '*(i)+(str(i+1)+' ')*(n-i)) # printing the same element so nested for loop is not required
    
    
    
    


   
#Example_35: TO PRINT  INVERTED PYRAMID PATTERN WITH FIXED ALPHABETS SYMBOL IN EVERY ROW
"""
A A A
 B B
  C
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print(' '*(i)+(chr(65+i)+' ')*(n-i)) # printing the same element so nested for loop is not required
    
    
    
    
    
    
   
#Example_36: TO PRINT  INVERTED PYRAMID PATTERN WITH DIGITS SYMBOL IN INCREASING ORDRER IN EVERY ROW
"""
1 2 3
 1 2
  1
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print(' '*(i),end=' ')
    for j in range(n-i):
        print(str(j+1),end=' ')
    print()
    
    
#Example_37: TO PRINT  INVERTED PYRAMID PATTERN WITH ALPHABETS SYMBOL IN INCREASING ORDRER IN EVERY ROW
"""
A B C
 A B
  A
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print(' '*(i),end=' ')
    for j in range(n-i):
        print(chr(65+j),end=' ')
    print()
    
    
    
    
    
    
#Example_38: TO PRINT INVERTED PYRAMID PATTERN WITH DIGITS SYMBOL IN DESCENDING ORDRER IN EVERY ROW
"""
3 2 1
 3 2
  3
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print(' '*(i),end=' ')
    for j in range(n-i):
        print(str(n-j),end=' ')
    print()
    
    
    
    
    
#Example_39: TO PRINT INVERTED PYRAMID PATTERN WITH ALPHABETS SYMBOL IN DESCENDING ORDRER IN EVERY ROW
"""
C B A
 C B
  C
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows
    print(' '*(i),end=' ')
    for j in range(n-i):
        print(chr(64+n-j),end=' ')
    print()
    
    
    
    
    
    
       
#Example_40: TO PRINT DIAMOND PATTERN WITH * SYMBOLS
"""
  *
 * *
* * *                       We will consider this problem in two parts
 * *                         -part_1. consider as pyramid
  *                          -part_2. consider as inverted pyramid
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows=====PART_1
    print(' '*(n-i-1)+"* "*(i+1)) # printing the same element so nested for loop is not required
for i in range(n-1):#loop will be executed  for 3 times/rows====PART_2
    print(' '*(i+1)+"* "*(n-i-1)) # printing the same element so nested for loop is not required  
    
    
    
    
    
    
#Example_41: TO PRINT DIAMOND PATTERN WITH FIXED DIGITS SYMBOLS IN EVERY ROW
"""
  1
 2 2
3 3 3
 2 2
  1
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows=====PART_1
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1)) # printing the same element so nested for loop is not required
for i in range(n-1):#loop will be executed  for 3 times/rows====PART_2
    print(' '*(i+1)+(str(n-i-1)+' ')*(n-i-1)) # printing the same element so nested for loop is not required  
    
    
    
    
    
    
    
#Example_42: TO PRINT DIAMOND PATTERN WITH FIXED ALPHABTES SYMBOLS IN EVERY ROW
"""
  A
 B B
C C C
 B B
  A
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows=====PART_1
    print(' '*(n-i-1)+(chr(65+i)+' ')*(i+1)) # printing the same element so nested for loop is not required
for i in range(n-1):#loop will be executed  for 3 times/rows====PART_2
    print(' '*(i+1)+(chr(63+n-i)+' ')*(n-i-1)) # printing the same element so nested for loop is not required  
    
    
    
    
#Example_43: TO PRINT DIAMOND PATTERN WITH DIGITS SYMBOLS IN ASCENDING ORDER IN EVERY ROW
"""
  1
 1 2
1 2 3
 1 2
  1
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows=====PART_1
    print(' '*(n-i-1),end=' ')
    for j in range(i+1):
        print(str(j+1),end=' ')
    print()
for i in range(n-1):#loop will be executed  for 3 times/rows====PART_2
    print(' '*(i+1),end=' ')
    for j in range(n-i-1): 
        print(str(j+1),end=' ')
    print()
    
    
    
    
    
    
    
#Example_44: TO PRINT DIAMOND PATTERN WITH ALPHABETS SYMBOLS IN ASCENDING ORDER IN EVERY ROW
"""
  A
 A B
A B C
 A B
  A
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows=====PART_1
    print(' '*(n-i-1),end=' ')
    for j in range(i+1):
        print(chr(65+j),end=' ')
    print()
for i in range(n-1):#loop will be executed  for 3 times/rows====PART_2
    print(' '*(i+1),end=' ')
    for j in range(n-i-1): 
        print(chr(65+j),end=' ')
    print()





#Example_45: TO PRINT DIAMOND PATTERN WITH DIGITS SYMBOLS IN DESCEBDING ORDER IN EVERY ROW
"""
  3
 3 2
3 2 1
 3 2
  3
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows=====PART_1
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print(str(n-j),end=' ')
    print()
for i in range(n-1):#loop will be executed  for 3 times/rows====PART_2
    print(' '*(i+1),end='')
    for j in range(n-i-1): 
        print(str(n-j),end=' ')
    print()
    
    
    
    
    
    
#Example_46: TO PRINT DIAMOND PATTERN WITH ALPHABETS SYMBOLS IN DESCENDING ORDER IN EVERY ROW
"""
  C
 C B
C B A
 C B
  C
"""
n=int(input("enter number of rows:"))
for i in range(n):#loop will be executed  for 3 times/rows=====PART_1
    print(' '*(n-i-1),end=' ')
    for j in range(i+1):
        print(chr(64+n-j),end=' ')
    print()
for i in range(n-1):#loop will be executed  for 3 times/rows====PART_2
    print(' '*(i+1),end=' ')
    for j in range(n-i-1): 
        print(chr(64+n-j),end=' ')
    print()
    
    
    
    
    
    
#Example_47: TO PRINT  RIGHT HALF DIAMOND PATTERN WITH * SYMBOLS
"""
*
* *
* * *
* *
*
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print("* "*(i+1))
for i in range(n-1):#PART_2
    print("* "*(n-i-1))
    
    
    
    
    
    
    
#Example_48: TO PRINT  RIGHT HALF DIAMOND PATTERN WITH FIXED DIGITS SYMBOLS IN EVERY ROW
"""
1
2 2
3 3 3
2 2
1
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print((str(i+1)+" ")*(i+1))
for i in range(n-1):#PART_2
    print((str(n-i-1)+" ")*(n-i-1))
    
    
    
    
    
    
    
#Example_49: TO PRINT  RIGHT HALF DIAMOND PATTERN WITH FIXED ALPHABETS SYMBOLS IN EVERY ROW
"""
A
B B
C C C
B B
A
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print((chr(65+i)+" ")*(i+1))
for i in range(n-1):#PART_2
    print((chr(63+n-i)+" ")*(n-i-1))
    
    
    
    
    
    
#Example_50: TO PRINT RIGHT HALF DIAMOND PATTERN WITH DIGITS SYMBOLS IN ASCENDING ORDER IN EVERY ROW
"""
1
1 2
1 2 3             [nested for loop is required]
1 2
1
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    for j in range(i+1):
        print(str(j+1),end=' ') 
    print()  
for i in range(n-1):#PART_2
    for j in range(n-i-1):
        print(str(j+1),end=' ')
    print()
    
    
    
    
    
#Example_51: TO PRINT RIGHT HALF DIAMOND PATTERN WITH ALPHABETS SYMBOLS IN ASCENDING ORDER IN EVERY ROW
"""
A
A B
A B C 
A B
A
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    for j in range(i+1):
        print(chr(65+j),end=' ') 
    print()  
for i in range(n-1):#PART_2
    for j in range(n-i-1):
        print(chr(65+j),end=' ')
    print()





#Example_52: TO PRINT RIGHT HALF DIAMOND PATTERN WITH DIGITS SYMBOLS IN DESCENDING ORDER IN EVERY ROW
"""
3
3 2
3 2 1
3 2
3
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    for j in range(i+1):
        print(str(n-j),end=' ') 
    print()  
for i in range(n-1):#PART_2
    for j in range(n-i-1):
        print(str(n-j),end=' ')
    print()
    
    
    
    
    
    
#Example_53: TO PRINT RIGHT HALF DIAMOND PATTERN WITH ALPHABETS SYMBOLS IN DESCENDING ORDER IN EVERY ROW
"""
C
C B
C B A
C B
C
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    for j in range(i+1):
        print(chr(64+n-j),end=' ') 
    print()  
for i in range(n-1):#PART_2
    for j in range(n-i-1):
        print(chr(64+n-j),end=' ')
    print()
    
    
    
    
    
    
    

#Example_54: TO PRINT LEFT HALF DIAMOND PATTERN WITH * SYMBOLS
"""
    * (4 BLANK SPACES=2 ACTUAL BLANK SPACES & 1 STAR)  
  * * (2 BLANK SPACES=1 ACTUAL BLANK SPACES & 2 STAR)  
* * * (0 BLANK SPACES=0 ACTUAL BLANK SPACES & 3 STAR)      [no need for nested for loop]
  * * (2 BLANK SPACES=1 ACTUAL BLANK SPACES & 2 STAR)
    * (4 BLANK SPACES=2 ACTUAL BLANK SPACES & 1 STAR)
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print("  "*(n-i-1)+"* "*(i+1)) #"  " means blank space followed by blank space separator===2  Actual blank spaces/in images
for i in range(n-1):  #PART_1
    print("  "*(i+1)+"* "*(n-i-1))
          
          
          
          
#Example_55: TO PRINT LEFT HALF DIAMOND PATTERN WITH FIXED DIGITS SYMBOLS IN EVERY ROW
"""
    1 (4 BLANK SPACES=2 ACTUAL BLANK SPACES & 1 STAR)  
  2 2 (2 BLANK SPACES=1 ACTUAL BLANK SPACES & 2 STAR)  
3 3 3 (0 BLANK SPACES=0 ACTUAL BLANK SPACES & 3 STAR)      [no need for nested for loop]
  2 2 (2 BLANK SPACES=1 ACTUAL BLANK SPACES & 2 STAR)
    1 (4 BLANK SPACES=2 ACTUAL BLANK SPACES & 1 STAR)
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print("  "*(n-i-1)+(str(i+1)+' ')*(i+1)) #"  " means blank space followed by blank space separator===2  Actual blank spaces/in images
for i in range(n-1):  #PART_1
    print("  "*(i+1)+(str(n-i-1)+' ')*(n-i-1))
    
    
    
    
    
    
#Example_56: TO PRINT LEFT HALF DIAMOND PATTERN WITH FIXED ALPHABETS SYMBOLS IN EVERY ROW
"""
    A(4 BLANK SPACES=2 ACTUAL BLANK SPACES & 1 STAR)  
  B B(2 BLANK SPACES=1 ACTUAL BLANK SPACES & 2 STAR)  
C C C(0 BLANK SPACES=0 ACTUAL BLANK SPACES & 3 STAR)      [no need for nested for loop]
  B B(2 BLANK SPACES=1 ACTUAL BLANK SPACES & 2 STAR)
    A
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print("  "*(n-i-1)+(chr(65+i)+' ')*(i+1)) #"  " means blank space followed by blank space separator===2  Actual blank spaces/in images
for i in range(n-1):  #PART_1
    print("  "*(i+1)+(chr(63+n-i)+' ')*(n-i-1))
    
    
    
    
    
    
#Example_57: TO PRINT LEFT HALF DIAMOND PATTERN WITH DIGITS SYMBOLS IN ASCENDING ORDER IN EVERY ROW
"""
    1(4 BLANK SPACES=2 ACTUAL BLANK SPACES & 1 STAR)  
  1 2(2 BLANK SPACES=1 ACTUAL BLANK SPACES & 2 STAR)  
1 2 3(0 BLANK SPACES=0 ACTUAL BLANK SPACES & 3 STAR)      [no need for nested for loop]
  1 2(2 BLANK SPACES=1 ACTUAL BLANK SPACES & 2 STAR)
    1
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print("  "*(n-i-1),end='') #"  " means blank space followed by blank space separator===2  Actual blank spaces/in images  also end=''/empty because we have to takes digits after spaces
    for j in range(i+1):
        print(str(j+1),end=' ')
    print()       
for i in range(n-1):  #PART_1
    print("  "*(i+1),end='')
    for j in range(n-i-1):
        print(str(j+1),end=' ')
    print()
    
    
    
#Example_58: TO PRINT LEFT HALF DIAMOND PATTERN WITH ALPHABETS SYMBOLS IN ASCENDING ORDER IN EVERY ROW
"""
    A(4 BLANK SPACES=2 ACTUAL BLANK SPACES & 1 STAR)  
  A B(2 BLANK SPACES=1 ACTUAL BLANK SPACES & 2 STAR)  
A B C(0 BLANK SPACES=0 ACTUAL BLANK SPACES & 3 STAR)      [no need for nested for loop]
  A B(2 BLANK SPACES=1 ACTUAL BLANK SPACES & 2 STAR)
    A
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print("  "*(n-i-1),end='') #"  " means blank space followed by blank space separator===2  Actual blank spaces/in images  also end=''/empty because we have to takes digits after spaces
    for j in range(i+1):
        print(chr(65+j),end=' ')
    print()       
for i in range(n-1):  #PART_1
    print("  "*(i+1),end='')
    for j in range(n-i-1):
        print(chr(65+j),end=' ')
    print()
    
    
    
    
    
    
    
    
#Example_59: TO PRINT LEFT HALF DIAMOND PATTERN WITH DIGITS SYMBOLS IN DESCENDING ORDER IN EVERY ROW
"""
    3(4 BLANK SPACES=2 ACTUAL BLANK SPACES & 1 STAR)  
  3 2(2 BLANK SPACES=1 ACTUAL BLANK SPACES & 2 STAR)  
3 2 1(0 BLANK SPACES=0 ACTUAL BLANK SPACES & 3 STAR)      [no need for nested for loop]
  3 2(2 BLANK SPACES=1 ACTUAL BLANK SPACES & 2 STAR)
    3
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print("  "*(n-i-1),end='') #"  " means blank space followed by blank space separator===2  Actual blank spaces/in images  also end=''/empty because we have to takes digits after spaces
    for j in range(i+1):
        print(str(n-j),end=' ')
    print()       
for i in range(n-1):  #PART_1
    print("  "*(i+1),end='')
    for j in range(n-i-1):
        print(str(n-j),end=' ')
    print()
    
    
    
    
    
#Example_60: TO PRINT LEFT HALF DIAMOND PATTERN WITH ALPHABTES SYMBOLS IN DESCENDING ORDER IN EVERY ROW
"""
    C(4 BLANK SPACES=2 ACTUAL BLANK SPACES & 1 STAR)  
  C B(2 BLANK SPACES=1 ACTUAL BLANK SPACES & 2 STAR)  
C B A(0 BLANK SPACES=0 ACTUAL BLANK SPACES & 3 STAR)      [no need for nested for loop]
  C B(2 BLANK SPACES=1 ACTUAL BLANK SPACES & 2 STAR)
    C
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print("  "*(n-i-1),end='') #"  " means blank space followed by blank space separator===2  Actual blank spaces/in images  also end=''/empty because we have to takes digits after spaces
    for j in range(i+1):
        print(chr(64+n-j),end=' ')
    print()       
for i in range(n-1):  #PART_1
    print("  "*(i+1),end='')
    for j in range(n-i-1):
        print(chr(64+n-j),end=' ')
    print()
    
    
    
    
    
    
#Example_61.1: TO PRINT TOP  HALF HALLOW DIAMOND PATTERN WITH * SYMBOLS 
"""
PART_1:TOP HALF HALLOW DIAMOND PATTERN
    *                [ "  " X 2 TIMES THEN STAR]                                             
  *  *               [ "  " X 1 TIMES THEN STAR]  # =====FOR PRINTING FIRST STAR IN EACH ROW  /HERE (N-i-1) times spaces("  ") in each row & 1 star(there is no need for nested loop as there same value in each row)
*      *             [ "  " X 0 TIMES THEN STAR]
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print("  "*(n-i-1)+"* ",end='')
    if i>=1:                                     # CHECK TO PRINT SECOND STAR FROM 2ND ROW ONWARDS 
        print("  "*(2*i-1)+"*",end='')          # ====== FOR PRINTING SECOND STAR BETWEEN THE SPACES.THE TOTAL SPACES BETWEEN TWO STAR IS (2*i-1)
    print()
#Example_61.2: TO PRINT BOTTOM HALF HALLOW DIAMOND PATTERN WITH * SYMBOLS
"""
PART_2:BOTTOM HALF HALLOW DIAMOND PATTERN
*      *              [ "  " X 0TIMES THEN STAR]                                             
 *   *                [ "  " X 1 TIMES THEN STAR]  # =====FOR PRINTING FIRST STAR IN EACH ROW  /HERE (i) times spaces("  ") in each row & 1 star (there is no need for nested loop as there same value in each row)
   *                  [ "  " X 2 TIMES THEN STAR]
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print("  "*(i)+"* ",end='')
    if i<(n-1):                                 # CHECK TO PRINT SECOND STAR FROM 2ND ROW ONWARDS 
        print("  "*(n-2*i)+"*",end='')        # ====== FOR PRINTING SECOND STAR BETWEEN THE SPACES.THE TOTAL SPACES BETWEEN TWO STAR IS (n-i-1)
    print()
#Example_61.3: TO PRINT COMPLETE HALLOW DIAMOND PATTERN WITH * SYMBOLS
"""
    *                  [ "  " X 2 TIMES THEN STAR]                                             
  *   *                [ "  " X 1 TIMES THEN STAR]  # =====FOR PRINTING FIRST STAR IN EACH ROW  /HERE (N-i-1) times spaces("  ") in each row & 1 star(there is no need for nested loop as there same value in each row)
*       *              [ "  " X 0 TIMES THEN STAR]                                                            
  *   *                [ "  " X 1 TIMES THEN STAR]  # =====FOR PRINTING FIRST STAR IN EACH ROW  /HERE (i) times spaces("  ") in each row & 1 star (there is no need for nested loop as there same value in each row)
    *                  [ "  " X 2 TIMES THEN STAR]

"""
n=int(input("enter number of rows:"))            
for i in range(n):#PART_1:TOP HALF HALLOW DIAMOND PATTERN
    print("  "*(n-i-1)+"* ",end='')
    if i>=1:                                     # CHECK TO PRINT SECOND STAR FROM 2ND ROW ONWARDS 
        print("  "*(2*i-1)+"*",end='')           # ====== FOR PRINTING SECOND STAR BETWEEN THE SPACES.THE TOTAL SPACES BETWEEN TWO STAR IS (2*i-1)
    print()    
for i in range(n-1):#PART_2:BOTTOM HALF HALLOW DIAMOND PATTERN
    print("  "*(i+1)+"* ",end='')
    if i<(n-1-1):                                 # CHECK TO PRINT SECOND STAR FROM 2ND ROW ONWARDS 
        print("  "*(i+1)+"*",end='')          # ====== FOR PRINTING SECOND STAR BETWEEN THE SPACES.THE TOTAL SPACES BETWEEN TWO STAR IS (n-i-1)
    print()







         
#Example_62: TO PRINT TOP  HALF HALLOW DIAMOND PATTERN WITH FIXED DIGITS SYMBOLS 
"""
    1               [ "  " X 2 TIMES THEN STAR]                                             
  2   2              [ "  " X 1 TIMES THEN STAR]  # =====FOR PRINTING FIRST STAR IN EACH ROW  /HERE (N-i-1) times spaces("  ") in each row & 1 star(there is no need for nested loop as there same value in each row)
3       3            [ "  " X 0 TIMES THEN STAR]
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print("  "*(n-i-1)+(str(i+1)+" "),end='')
    if i>=1:                                     # CHECK TO PRINT SECOND STAR FROM 2ND ROW ONWARDS 
        print("  "*(2*i-1)+(str(i+1)+" "),end='')          # ====== FOR PRINTING SECOND STAR BETWEEN THE SPACES.THE TOTAL SPACES BETWEEN TWO STAR IS (2*i-1)
    print()
    
    
    
    
    
    
#Example_63: TO PRINT TOP  HALF HALLOW DIAMOND PATTERN WITH FIXED ALPHABETS SYMBOLS 
"""
    A               [ "  " X 2 TIMES THEN STAR]                                             
  B   B              [ "  " X 1 TIMES THEN STAR]  # =====FOR PRINTING FIRST STAR IN EACH ROW  /HERE (N-i-1) times spaces("  ") in each row & 1 star(there is no need for nested loop as there same value in each row)
C       C  
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print("  "*(n-i-1)+(chr(65+i)+" "),end='')
    if i>=1:                                     # CHECK TO PRINT SECOND STAR FROM 2ND ROW ONWARDS 
        print("  "*(2*i-1)+(chr(65+i)+" "),end='')          # ====== FOR PRINTING SECOND STAR BETWEEN THE SPACES.THE TOTAL SPACES BETWEEN TWO STAR IS (2*i-1)
    print()
    
    
  
  
    
    
#Example_64: TO PRINT TOP  HALF HALLOW DIAMOND PATTERN WITH FIXED DIGITS SYMBOLS IN DESCENDING ORDER
"""
    3              [ "  " X 2 TIMES THEN STAR]                                             
  2   2              [ "  " X 1 TIMES THEN STAR]  # =====FOR PRINTING FIRST STAR IN EACH ROW  /HERE (N-i-1) times spaces("  ") in each row & 1 star(there is no need for nested loop as there same value in each row)
1       1  
""" 
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print("  "*(n-i-1)+(str(n-i)+" "),end='')
    if i>=1:                                     # CHECK TO PRINT SECOND STAR FROM 2ND ROW ONWARDS 
        print("  "*(2*i-1)+(str(n-i)+" "),end='')          # ====== FOR PRINTING SECOND STAR BETWEEN THE SPACES.THE TOTAL SPACES BETWEEN TWO STAR IS (2*i-1)
    print()
    
    
    
    
    
    
#Example_65: TO PRINT TOP  HALF HALLOW DIAMOND PATTERN WITH FIXED DIGITS SYMBOLS IN DESCENDING ORDER
"""
    C              [ "  " X 2 TIMES THEN STAR]                                             
  B   B              [ "  " X 1 TIMES THEN STAR]  # =====FOR PRINTING FIRST STAR IN EACH ROW  /HERE (N-i-1) times spaces("  ") in each row & 1 star(there is no need for nested loop as there same value in each row)
A       A  
"""
n=int(input("enter number of rows:"))
for i in range(n):  #PART_1
    print("  "*(n-i-1)+(chr(64+n-i)+" "),end='')
    if i>=1:                                     # CHECK TO PRINT SECOND STAR FROM 2ND ROW ONWARDS 
        print("  "*(2*i-1)+(chr(64+n-i)+" "),end='')          # ====== FOR PRINTING SECOND STAR BETWEEN THE SPACES.THE TOTAL SPACES BETWEEN TWO STAR IS (2*i-1)
    print()
    
    
    
    
    
    
    
    
#Example_66: TO PRINT COMPLETE HALLOW DIAMOND PATTERN WITH FIXED DIGITS SYMBOLS IN EVERY ROW
"""
    1                 [ "  " X 2 TIMES THEN STAR]                                             
  2   2                [ "  " X 1 TIMES THEN STAR]  # =====FOR PRINTING FIRST STAR IN EACH ROW  /HERE (N-i-1) times spaces("  ") in each row & 1 star(there is no need for nested loop as there same value in each row)
3       3              [ "  " X 0 TIMES THEN STAR]                                                            
  2   2               [ "  " X 1 TIMES THEN STAR]  # =====FOR PRINTING FIRST STAR IN EACH ROW  /HERE (i) times spaces("  ") in each row & 1 star (there is no need for nested loop as there same value in each row)
    1                  [ "  " X 2 TIMES THEN STAR]
"""
n=int(input("enter number of rows:"))            
for i in range(n):#PART_1:TOP HALF HALLOW DIAMOND PATTERN
    print("  "*(n-i-1)+(str(i+1)+" "),end='')
    if i>=1:                                     # CHECK TO PRINT SECOND STAR FROM 2ND ROW ONWARDS 
        print("  "*(2*i-1)+(str(i+1)+" "),end='')           # ====== FOR PRINTING SECOND STAR BETWEEN THE SPACES.THE TOTAL SPACES BETWEEN TWO STAR IS (2*i-1)
    print()    
for i in range(n-1):#PART_2:BOTTOM HALF HALLOW DIAMOND PATTERN
    print("  "*(i+1)+(str(n-i-1)+" "),end='')
    if i<(n-1-1):                                 # CHECK TO PRINT SECOND STAR FROM 2ND ROW ONWARDS 
        print("  "*(i+1)+(str(n-i-1)+" "),end='')          # ====== FOR PRINTING SECOND STAR BETWEEN THE SPACES.THE TOTAL SPACES BETWEEN TWO STAR IS (n-i-1)
    print()
    
    




    


        



    
    
    



    
    


    
    
    
    

    
 
        



        
        
        
        
        
        
    
    

    
    
    







    
    
    
    

    




    


