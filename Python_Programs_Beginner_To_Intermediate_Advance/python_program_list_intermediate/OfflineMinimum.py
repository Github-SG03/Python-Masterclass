def off_line_minimum(strArr):
    nums = []  # Store numbers before encountering 'E'
    result = []  # Store extracted minimum values

    for item in strArr:
        if item == "E":
            if nums:
                nums.sort()  # Ensure the smallest element is at index 0
                result.append(str(nums.pop(0)))  # Extract the smallest element
        else:
            nums.append(int(item))  # Store numbers for later extraction

    return ",".join(result)  # Return the result as a string

# Example Usage
print(off_line_minimum(["5","4","6","E","1","7","E","E","3","2"]))  # Output: 4,1,5
print(off_line_minimum(["1","2","E","E","3"]))  # Output: 1,2
print(off_line_minimum(["4","E","1","E","2","E","3","E"]))  # Output: 4,1,2,3
