#####################################COMMAND LINE PROGRAMMING IN PYTHON################################################################################

#Example_1:find the of 'argv'
from sys import argv
print(type(argv))


#Example_2:find the of values of 'argv'
from sys import argv
print(argv[0])
print(argv[1])
print(argv[2])




#Example_3: Let’s suppose there is a Python script for adding two numbers and the numbers are passed as command-line arguments.
import sys
# total arguments
n = len(argv)
print("Total arguments passed:", n)

# Arguments passed
print("list of arguments passed:", argv)
print("\nName of Python script:", argv[0])

print("\nArguments passed:", end = " ")
for i in range(1, n):
	print(argv[i], end = " ")
	
# Addition of numbers                                  #we can use
Sum = 0                                                #args=argv[1:]
# Using argparse module                                #sum=0
for i in range(1, n):                                  #for x in args: 
	Sum += int(argv[i])                                #  sum=sum+ x	#type error as 'x' is here 'string' type
print("\n\nResult for sum:", Sum)                      #print("summation is:",sum)



'''
#Example_4: arguments are by-default is string in natura
args=argv[1:]
sum=0
for x in args:
    sum=sum+x
print("summation of command line arguments is:",sum)
'''



#Example_5:Real time application of comman line arguments
#File_Merger_Application
#note: for client purpose(real-time scenario) we can use file of their use which can be taken from command line
f1=open("file_1.txt")             #'argv[1]' instead of "file_1.txt"
f2=open("file_2.txt")             #'argv[2]' instead of "file_2.txt"
f3=open("output_1.txt",'w+')      #'argv[3]' instead of "file_3.txt"
for x in f1:                       
    f3.write(x)
for x in f2:
    f3.write(x)
f1.close()
f2.close()



