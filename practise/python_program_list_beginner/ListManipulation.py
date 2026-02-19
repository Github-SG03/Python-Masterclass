#1.Swap function to swap the 2 list elements(any)
def swapList(list):
    
    # Storing the first and last element 
    # as a pair in a tuple variable get
    get = list[-1], list[0]
    
    # unpacking those elements
    list[0], list[-1] = get
    
    return list
    
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))



######################################################################################################################################
#2.Swap function to swap the 2 list elements(any) using temp variable
a = [10, 20, 30, 40, 50]

# Using a temporary variable to swap elements at index 2 and 4
temp = a[2]
a[2] = a[4]
a[4] = temp

print(a)



######################################################################################################################################
#3.To find an element in the list
a = [10, 20, 30, 40, 50]
# Check if 30 exists in the list using a loop
key = 30
flag = False

for val in a:
    if val == key:
        flag = True
        break

if flag:
    print("Element exists in the list")
else:
    print("Element does not exist")




######################################################################################################################################
#4.To delete all element in list
a = [1, 2, 3, 4, 5]
del a[:]
print("List after using del:", a)




######################################################################################################################################
#5 To create a reversed list using insert() method &l oop in Python
a = [1, 2, 3, 4, 5]

# Initialize an empty list to store reversed element
res = []

# Loop through each item and insert it at the beginning of new list
for val in a:
    res.insert(0, val)
print(res)



######################################################################################################################################
#6.to find the largest number in a list using loop not using max() function
#note: it will also be applicable for finding the smallest number in a list but change the condition in line 88
a = [10, 24, 76, 23, 12]

# Assuming first element is largest.
largest = a[0]

# Iterate through list and find largest
for val in a:
    if val > largest:
      
        # If current element is greater than largest update it
        largest = val

print(largest)



######################################################################################################################################
#7.To find the second largest number in a list
a = [10, 20, 4, 45, 99]

# Initialize largest (max1)
# and second largest (max2) to negative infinity
max1 = max2 = float('-inf')

# Loop through each number in list
for n in a:
  
    # If the current number is greater than largest found so far
    if n > max1:
      
        # Update second largest to the previous largest
        max2 = max1  
        
        # Update largest to the current number
        max1 = n     
        
    # If current number is less than largest but greater than second largest
    elif n > max2 and n != max1:
      
        # Update second largest to current number
        max2 = n  

print(max2)



######################################################################################################################################
#8. Python program to find N largest element from given list of integers

# Function returns N largest elements
def Nmaxelements(list1, N):
	final_list = []

	for i in range(0, N):
		max1 = 0

		for j in range(len(list1)):
			if list1[j] > max1:
				max1 = list1[j]

		list1.remove(max1)
		final_list.append(max1)

	print(final_list)


# Driver code
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2

# Calling the function
Nmaxelements(list1, N)




######################################################################################################################################
#9.To find even numbers in a list and if so print the list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterate through each element in the list
for val in a:
  
    # Checks if a number is divisible by 2 (i.e., even).
    if val % 2 == 0:
        print(val, end = " ")



######################################################################################################################################
#10.To remove multiple elements from a list in Python
a = [10, 20, 30, 40, 50, 60, 70]

# Elements to remove
remove = [20, 40, 60]

# Remove elements using a simple for loop
res = []

for val in a:
    if val not in remove:
        res.append(val)

print(res)



######################################################################################################################################
#11.To count the number of occurrences of an element in a list
a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]

# Initial count is zero
count = 0

# Iterate over the list
for val in a:
  
      # If num is equal to 3 
    if val == 3:
      
        # Increase the counter
        count += 1

print(count)



######################################################################################################################################
#12.To find the duplicate elements in a list
a = [1, 2, 3, 1, 2, 4, 5, 6, 5]

# Initialize an empty set to store seen elements
s = set()

# List to store duplicates
dup = []

for n in a:
    if n in s:
        dup.append(n)
    else:
        s.add(n)

print(dup)



######################################################################################################################################
#13.To remove epmty tuples from a list
a = [(1, 2), (), (3, 4), (), (5,)]
res = []

# Iterate over the list 'a'
for t in a:
  
    # If tuple is not empty then add it to res.
    if t:
        res.append(t)

print(res)



######################################################################################################################################
#13.To find the sum of digits of a number in al list
# Function to sum digits of a number
def dsum(val):
    total = 0  # Initialize the total sum of digits
    
    # Loop until number is reduced to zero
    while val > 0:
      
        # Add last digit to the total
        total += val % 10  
        
        # Remove last digit from number
        val //= 10  
    
    # Return total sum of digits
    return total  

a = [123, 456, 789]

# Calculate sum of digits for each number
# using list comprehension
res = [dsum(val) for val in a]
print(res)



######################################################################################################################################
#14.To brak the list into chunks of size n
l = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
 
# How many elements each list should have 
n = 4
 
# using list comprehension 
x = [l[i:i + n] for i in range(0, len(l), n)] 
print(x)



######################################################################################################################################
#15.1 To convert a string to a list of characters or words
s = "Geeks for Geeks"
# adds each character of string as an element in a list
a = list(s)
print(a)

#15.2 To convert a string to a list of characters or words
s = "Geeks,for,Geeks"
# Splits string into words based on comma (,).
a = s.split(',')
print(a)



######################################################################################################################################
#16.To covert a list of characters or words to integer list
a = ['2', '4', '6', '8']

# Iterating over list
for i in range(len(a)):
  
      # Converts each element to an integer
    a[i] = int(a[i])

print(a)




######################################################################################################################################
#17.Create a dictionary from a list
# Creating an empty dictionary
d = {}

# Adding list as value
d["1"] = [1, 2]
d["2"] = ["Geeks", "For", "Geeks"] 

print(d)




######################################################################################################################################
#18.To compare two list are equal are not
a = [1, 2, 3]
b = [1, 2, 3]

# Set a flag to True to assume lists are identical initially
flag = True

# Check if lengths of both lists are equal
if len(a) != len(b):
  
     # If lengths differ, set flag to False
    flag = False 
else:
  
    # Iterate over each element in lists
    for i in range(len(a)):   
      
        # Compare corresponding elements of both lists
        if a[i] != b[i]:
              
            # If any elements differ, set flag to False
            flag = False  
            
            # Exit the loop since we found a difference
            break  

print(flag)




######################################################################################################################################
#19.Python code to demonstrate to find strings with substrings using list comprehension

# Initializing list
test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']

# Printing original list
print("The original list is : " + str(test_list))

# Initializing substring
subs = 'Geek'

# using list comprehension
# to get string with substring
res = [i for i in test_list if subs in i]

# Printing result
print("All strings with given substring are : " + str(res))


######################################################################################################################################
#20.To find
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

# Find the union of lists
union_list = list(set(a).union(b))

print("Union lists:", union_list)



######################################################################################################################################
#21.To add
# Input lists
a = [1, 3, 4, 6, 8]
b = [4, 5, 6, 2, 10]

# Add corresponding elements using list comprehension
c = [a[i] + b[i] for i in range(len(a))]

# Print the result
print(c)



######################################################################################################################################
#21.To print unique elements from a list and also find its count
# taking an input list
input_list = [1, 2, 2, 5, 8, 4, 4, 8]

# taking an input list
l1 = []

# taking an counter
count = 0

# traversing the array
for item in input_list:
    if item not in l1:
        count += 1
        l1.append(item)

# printing the output
print("No of unique items are:", l1)
print("No of unique items are:", count)




######################################################################################################################################
#23. To find the median of a list
# Python3 code to demonstrate working of 
# Median of list 
# Using loop + "~" operator 

# initializing list 
test_list = [4, 5, 8, 9, 10, 17] 

# printing list 
print("The original list : " + str(test_list)) 

# Median of list 
# Using loop + "~" operator 
test_list.sort() 
mid = len(test_list) // 2
res = (test_list[mid] + test_list[~mid]) / 2

# Printing result 
print("Median of list is : " + str(res)) 




######################################################################################################################################
#24.Python3 code to demonstrate Separating odd and even index elements using naive method

# initializing list
test_list = [3, 6, 7, 8, 9, 2, 1, 5]

# printing original list
print("The original list : " + str(test_list))

# using naive method
# Separating odd and even index elements
odd_i = []
even_i = []
for i in range(0, len(test_list)):
	if i % 2:
		even_i.append(test_list[i])
	else :
		odd_i.append(test_list[i])

res = odd_i + even_i

# print result
print("Separated odd and even index list: " + str(res))


######################################################################################################################################




