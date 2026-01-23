## 1.Python 3 code to find sum of elements in given array
def _sum(arr):

	# initialize a variable
	# to store the sum
	# while iterating through
	# the array later
	sum = 0

	# iterate through the array
	# and add each element to the sum variable
	# one at a time
	for i in arr:
		sum = sum + i

	return(sum)

# main function
if __name__ == "__main__":
	# input values to list
	arr = [12, 3, 4, 15]

	# calculating length of array
	n = len(arr)
	# calling function ans store the sum in ans
	ans = _sum(arr)
	# display length of array
	print('Sum of the array is ', n)
	# display sum
	print('Sum of the array is ', ans)




######################################################################################################################################

#2.Python3 program to find maximum in arr[] of size n
def largest(arr, n):

	# Initialize maximum element
	max = arr[0]

	# Traverse array elements from second
	# and compare every element with
	# current max
	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max


# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)



######################################################################################################################################

#3.Python program to split array and move first part to end.
def splitArr(arr, n, k):
	for i in range(0, k):
		x = arr[0]
		for j in range(0, n-1):
			arr[j] = arr[j + 1]

		arr[n-1] = x

# main
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2

splitArr(arr, n, position)

for i in range(0, n):
	print(arr[i], end=' ')
	


######################################################################################################################################

#4.This code finds the remainder of the product of all the elements in the array arr divided by 'n'.
def findremainder(arr, len, n):
	product = 1
	for i in range(len):
		product = product * arr[i]
	return product % n


arr = [100, 10, 5, 25, 35, 14]
len = len(arr)
n = 11
print(findremainder(arr, len, n))


######################################################################################################################################

#5.function to rotate array by d(2) elements using temp array
def rotateArray(arr, n, d):
	temp = []
	i = 0
	while (i < d):
		temp.append(arr[i])
		i = i + 1
	i = 0
	while (d < n):
		arr[i] = arr[d]
		i = i + 1
		d = d + 1
	arr[:] = arr[: i] + temp
	return arr


# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))



######################################################################################################################################
##6.Python Program to check if given array is Monotonic to Check if given array is Monotonic

def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

# Driver program
A = [6, 5, 4, 4]

# Print required result
print(isMonotonic(A))