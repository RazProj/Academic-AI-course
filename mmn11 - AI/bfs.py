from collections import deque
from utils import is_goal, get_neighbors, restore_path_for_bfs_iddfs


# Breadth-First Search (BFS)
def bfs(start, goal):
    # Initialize queue with the starting state and its path
    queue = deque([(start, [start])])

    # Set to track visited states and avoid cycles
    visited = set()
    visited.add(tuple(start))  # Add the start state as visited

    # Counter to track the number of developed nodes
    developed_nodes_count = 0

    while queue:
        # Dequeue the front element (FIFO), containing the current state and its path
        state, path = queue.popleft()
        developed_nodes_count += 1  # Increment the developed count for each node expanded

        # Goal check: if the current state matches the goal, output the developed count and return the path
        if is_goal(state, goal):
            print("Quantity of nodes developed:", developed_nodes_count)
            return restore_path_for_bfs_iddfs(path)  # Restore the path if goal is reached

        # Explore neighbors of the current state
        for neighbor in get_neighbors(state):
            # Check if neighbor has not been visited to avoid revisiting
            if tuple(neighbor) not in visited:
                visited.add(tuple(neighbor))  # Mark neighbor as visited
                # Enqueue the neighbor with the updated path to reach it
                queue.append((neighbor, path + [neighbor]))

    # If no solution is found, print developed nodes count and return None
    print("Quantity of nodes developed:", developed_nodes_count)
    return False
