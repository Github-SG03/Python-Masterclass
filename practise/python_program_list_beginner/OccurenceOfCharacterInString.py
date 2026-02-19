# This program counts the number of occurrences of a character in a string.
count = 0
my_string = "Programiz"
my_char = "r"

for i in my_string:
    if i == my_char:
        count += 1

print(count)
