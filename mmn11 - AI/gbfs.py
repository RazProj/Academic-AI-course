import heapq
from heuristic_function import permutation_transpositions_count
from utils import is_goal, get_neighbors, restore_path_for_astar_and_gbfs


# Greedy Best-First Search
def gbfs(start, goal):
    # Priority queue to store nodes to explore; sorted by heuristic value h(n)
    frontier = []

    # Dictionary to keep track of the most efficient path to reach each node
    came_from = {}

    # Counter to track the number of developed nodes
    developed_nodes_count = 0

    # Push the initial state onto the priority queue with its heuristic value
    heapq.heappush(frontier, (permutation_transpositions_count(start, goal), start))
    came_from[tuple(start)] = None  # Mark the start state in came_from as the beginning of the path

    while frontier:
        # Pop the node with the lowest heuristic value from the priority queue
        _, current = heapq.heappop(frontier)

        # Goal check: if the current state matches the goal, reconstruct the path and return it
        if is_goal(current, goal):
            print("Quantity of nodes developed:", developed_nodes_count)
            # Reconstruct the path from start to goal using the came_from dictionary
            return restore_path_for_astar_and_gbfs(came_from, start, current, developed_nodes_count)

        # Expand the neighbors of the current node
        for neighbor in get_neighbors(current):
            neighbor_tuple = tuple(neighbor)  # Convert neighbor to tuple for hashable dictionary keys

            # Only proceed if this neighbor hasn't been visited yet
            if neighbor_tuple not in came_from:
                # Record the current state as the predecessor of this neighbor
                came_from[neighbor_tuple] = tuple(current)

                # Push the neighbor onto the priority queue with its heuristic value as priority
                heapq.heappush(frontier, (permutation_transpositions_count(neighbor, goal), neighbor))

        # Increment the developed nodes counter after processing all neighbors of the current node
        developed_nodes_count += 1

    print("Quantity of nodes developed:", developed_nodes_count)
    # Return False if no solution was found
    return False
