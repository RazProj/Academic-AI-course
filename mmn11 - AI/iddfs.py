from utils import is_goal, get_neighbors, restore_path_for_bfs_iddfs


# Depth-Limited Search (DLS)
def dls(state, goal, path, depth, visited, developed_count):
    # Base case: if depth is 0 and the current state is the goal, return the path and developed count
    if depth == 0 and is_goal(state, goal):
        return path, developed_count

    # If depth limit allows, expand neighbors
    if depth > 0:
        for neighbor in get_neighbors(state):
            # Check if the neighbor has not been visited to avoid cycles
            if tuple(neighbor) not in visited:
                visited.add(tuple(neighbor))  # Mark neighbor as visited
                developed_count += 1  # Increment the count for each node developed

                # Recursive call with reduced depth and updated path
                result, developed_count = dls(neighbor, goal, path + [neighbor], depth - 1, visited, developed_count)

                # If a solution is found, return it
                if result is not None:
                    return result, developed_count

                # Backtrack: remove neighbor from visited to allow other paths at this depth
                visited.remove(tuple(neighbor))

    # If no solution found at this depth, return None and the developed count so far
    return None, developed_count


# Iterative Deepening Search (IDDFS) with developed count
def iddfs(start, goal):
    depth = 0
    total_developed_count = 0  # Track total nodes developed across all depths

    # Loop indefinitely, incrementing depth at each iteration
    while True:
        visited = set()  # Track visited states at the current depth
        visited.add(tuple(start))  # Mark the start state as visited

        # Run depth-limited search (DLS) at the current depth
        result, developed_count = dls(start, goal, [start], depth, visited, 0)

        # Accumulate the total count of nodes developed across all depth levels
        total_developed_count += developed_count

        # If a solution is found at this depth level, print the total nodes developed and return the solution path
        if result is not None:
            print("Quantity of nodes developed:", total_developed_count)
            return restore_path_for_bfs_iddfs(result)

        # Increment the depth limit for the next iteration if no solution was found
        depth += 1
