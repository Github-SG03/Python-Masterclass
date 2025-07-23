def closest_enemy_1d(grid):
    player_index = grid.index(1)  # Find the player's position
    enemy_positions = [i for i, val in enumerate(grid) if val == 2]  # Find all enemies

    if not enemy_positions:
        return -1  # No enemies found

    return min(abs(player_index - enemy) for enemy in enemy_positions)  # Find the closest enemy

# Example usage
grid = [0, 0, 1, 0, 2, 2, 0, 2]
print(f"Closest enemy distance: {closest_enemy_1d(grid)}")
