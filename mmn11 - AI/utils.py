# if the current state matches the goal configuration
def is_goal(state, goal):
    return state == goal


# Function to get all possible neighbor states by moving the empty space (0)
def get_neighbors(state):
    moves = []  # List to hold the possible states after moving the empty space
    index = state.index(0)  # Find the current position of the empty space (0)

    # Directions that the empty space can move: left, right, up, and down
    directions = {'left': -1, 'right': 1, 'up': -3, 'down': 3}

    # Loop through each direction and check if the move is valid
    for direction, step in directions.items():
        new_index = index + step
        new_row, new_col = divmod(new_index, 3)  # Convert new index to row and column (3x3 grid)

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            # Create a new state by copying the current state
            new_state = state[:]
            # Swap the empty space (0) with the tile at the new index
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            moves.append(new_state)

    return moves


# Function to count the number of inversions in the given puzzle configuration
def get_inv_count(arr):
    inv_count = 0
    # Loop through all pairs of tiles to count inversions
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[i] > arr[j]:  # If a larger number comes before a smaller one, it's an inversion
                inv_count += 1
    return inv_count


def is_solvable(puzzle):
    inv_count = get_inv_count(puzzle)

    # A puzzle is solvable if the number of inversions is even
    return inv_count % 2 == 0


# Function to restore the path for BFS or IDDFS
def restore_path_for_bfs_iddfs(path):
    swap_path = []

    # Iterate through pairs of consecutive states in the solution path
    for i in range(1, len(path)):
        prev_state = path[i - 1]  # Previous state
        current_state = path[i]  # Current state

        # Find the index of the empty space (0) in the current state
        zero_index_curr = current_state.index(0)

        # The value that was swapped with the empty space in the previous state
        swapped_value = prev_state[zero_index_curr]
        # Add this swapped value to the swap path
        swap_path.append(swapped_value)

    return swap_path


# Function to restore the path for A* and Greedy Best-First Search (A* and GBFS)
def restore_path_for_astar_and_gbfs(came_from, start, goal, expanded_nodes_count):
    path = []  # List to store the path of tile swaps
    current = goal  # Start from the goal state

    # Reconstruct the path from the goal back to the start state
    while current != start:
        # Get the previous state from the came_from dictionary
        previous = came_from.get(tuple(current))

        # If there is no valid previous state, break (should not happen if the search worked correctly)
        if previous is None:
            break

        # Find the position of the empty space (0) in the current state
        zero_index_current = current.index(0)

        # The tile that was swapped with the empty space in the previous state
        swapped_value = previous[zero_index_current]
        # Add this swapped value to the path
        path.append(swapped_value)

        # Move to the previous state in the path
        current = previous

    # Reverse the path to get the order from start to goal
    path.reverse()

    # Return the restored path along with the number of expanded nodes
    return path, expanded_nodes_count
