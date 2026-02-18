def rectangle_area(strArr):
    # Parse the input to extract x, y coordinates
    points = [tuple(map(int, point.strip("()").split())) for point in strArr]

    # Extract unique x and y coordinates
    x_coords = set(x for x, y in points)
    y_coords = set(y for x, y in points)

    # Calculate width and height
    width = max(x_coords) - min(x_coords)
    height = max(y_coords) - min(y_coords)

    # Return the area of the rectangle
    return width * height

# Example Usage
print(rectangle_area(["(1 1)", "(1 3)", "(3 1)", "(3 3)"]))  # Output: 4
print(rectangle_area(["(0 0)", "(1 0)", "(1 1)", "(0 1)"]))  # Output: 1

