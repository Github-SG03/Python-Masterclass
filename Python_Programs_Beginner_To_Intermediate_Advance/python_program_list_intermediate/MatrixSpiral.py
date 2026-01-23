def matrix_spiral(strArr):
    # Convert string list to 2D matrix
    matrix = [list(map(int, row.strip("[]").split(","))) for row in strArr]

    # Initialize boundaries
    top, left = 0, 0
    bottom, right = len(matrix) - 1, len(matrix[0]) - 1
    result = []

    while top <= bottom and left <= right:
        # Move Right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1  # Move down

        # Move Down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1  # Move left

        if top <= bottom:
            # Move Left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1  # Move up

        if left <= right:
            # Move Up
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1  # Move right

    return ",".join(map(str, result))

# Example Usage
print(matrix_spiral(["[1, 2]", "[10, 14]"]))  # Output: 1,2,14,10
print(matrix_spiral(["[4, 5, 6, 5]", "[1, 1, 2, 2]", "[5, 4, 2, 9]"]))  # Output: 4,5,6,5,2,9,2,4,5,1,1,2
print(matrix_spiral(["[1, 2, 3]", "[4, 5, 6]", "[7, 8, 9]"]))  # Output: 1,2,3,6,9,8,7,4,5
