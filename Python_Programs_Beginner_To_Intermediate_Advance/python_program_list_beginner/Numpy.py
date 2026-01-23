import numpy as np

# Create an 8x3 integer array from a range between 10 to 34
array = np.arange(10, 34).reshape(8, 3)

# Split the array into four equal-sized sub-arrays
sub_arrays = np.array_split(array, 4)

# Print the sub-arrays
for i, sub_array in enumerate(sub_arrays):
    print(f"Sub-array {i+1}:\n{sub_array}\n")