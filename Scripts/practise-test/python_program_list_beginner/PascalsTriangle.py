def print_pascals_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    for row in triangle:
        print(" ".join(map(str, row)).center(n * 2))

# Example: Print Pascal’s Triangle for 5 rows
rows = int(input("Enter number of rows: "))
print_pascals_triangle(rows)
