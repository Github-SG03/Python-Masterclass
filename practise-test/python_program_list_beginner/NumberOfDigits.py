# This program will count the number of digits in a given number
num = 3452
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))
# Output: Number of digits: 4
