# Function to create a 2D array using two input digits
def create_2d_array(rows, cols):
    array = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter value for element [{i}][{j}]: "))
            row.append(value)
        array.append(row)
    return array

# Input for number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Create and print the 2D array
array = create_2d_array(rows, cols)
print("2D Array:")
for row in array:
    print(row)