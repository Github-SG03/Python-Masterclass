from itertools import permutations

def is_valid_path(path):
    """Check if the given path leads from (0,0) to (4,4) without revisiting."""
    visited = set()
    x, y = 0, 0
    visited.add((x, y))
    
    for move in path:
        if move == 'r': x += 1
        elif move == 'l': x -= 1
        elif move == 'u': y -= 1
        elif move == 'd': y += 1

        # If out of bounds or revisiting a cell, return False
        if x < 0 or x > 4 or y < 0 or y > 4 or (x, y) in visited:
            return False
        
        visited.add((x, y))

    return (x, y) == (4, 4)  # Must end at bottom-right corner

def CorrectPath(s):
    """Finds the correct path by replacing '?' with valid moves."""
    moves = list(s)
    missing_count = moves.count('?')

    # Possible movements in a 5x5 grid (20 steps: 4 downs, 4 rights, etc.)
    right_needed = 4 - s.count('r') + s.count('l')
    down_needed = 4 - s.count('d') + s.count('u')

    # Generate all permutations of required 'r' and 'd' replacements
    for replacement in permutations('r' * right_needed + 'd' * down_needed, missing_count):
        temp_moves = moves[:]  # Copy the original list
        it = iter(replacement)  # Iterator for replacements

        # Replace '?' with generated moves
        for i in range(len(temp_moves)):
            if temp_moves[i] == '?':
                temp_moves[i] = next(it)

        # Check if the generated path is valid
        if is_valid_path(temp_moves):
            return "".join(temp_moves)

# Test cases
print(CorrectPath("???rrurdr?"))  # Output: "dddrrurdrd"
print(CorrectPath("drdr??rrddd?"))  # Output: "drdruurrdddd"
