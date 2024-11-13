def permutation_transpositions_count(current_state, goal_state):
    visited = [False] * len(current_state)  # Track visited indices
    transpositions = 0

    # Create a mapping from tile to its position in the goal state
    goal_positions = {}
    for idx, tile in enumerate(goal_state):
        goal_positions[tile] = idx

    # Iterate over each element in the current state
    for i in range(len(current_state)):
        if visited[i] or current_state[i] == goal_state[i]:
            continue

        # Start a new cycle
        cycle_length = 0
        j = i

        # Follow the cycle until we revisit the starting index
        while not visited[j]:
            visited[j] = True
            j = goal_positions[current_state[j]]  # Move to the next index in the cycle
            cycle_length += 1

        # Only add to transpositions if there's a cycle
        if cycle_length > 0:
            transpositions += cycle_length - 1  # Each cycle requires (length - 1) transpositions

    return transpositions
