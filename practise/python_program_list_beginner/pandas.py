import pandas as pd
import numpy as np

# Create an array with 16 elements
array = np.arange(1, 17)

# Convert the array to a pandas DataFrame
df = pd.DataFrame(array, columns=['element'])

# Split the DataFrame into four equal-sized sub-arrays
sub_arrays = np.array_split(df, 4)

# Print the sub-arrays
for i, sub_array in enumerate(sub_arrays):
    print(f"Sub-array {i+1}:\n{sub_array}\n")