#Python Program to Get Line Count of a File
num_of_lines = sum(1 for l in open('my_file.txt'))
print(num_of_lines)
# Output: 3



