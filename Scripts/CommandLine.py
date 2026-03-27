#####################################COMMAND LINE PROGRAMMING IN PYTHON################################################################################
from pathlib import Path

#Example_1:find the of 'argv'
from sys import argv
print(type(argv))


#Example_2:find the of values of 'argv'
from sys import argv
print(argv[0])
print(argv[1] if len(argv) > 1 else "No first argument provided")
print(argv[2] if len(argv) > 2 else "No second argument provided")




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
DATASET_DIR = Path(__file__).resolve().parent.parent / "datasets"
if len(argv) >= 4:
    file_1 = DATASET_DIR / "File1.txt"
    file_2 = DATASET_DIR / "File2.txt"
    output_file = DATASET_DIR / "output_1.txt"
    with file_1.open() as f1, file_2.open() as f2, output_file.open("w+") as f3:
        for x in f1:
            f3.write(x)
        for x in f2:
            f3.write(x)
else:
    print("Skipping file merge example because no file arguments were supplied.")



