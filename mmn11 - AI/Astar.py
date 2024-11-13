import heapq
from utils import is_goal, get_neighbors, restore_path_for_astar_and_gbfs
from heuristic_function import permutation_transpositions_count


def a_star(start, goal):
    # Priority queue to store nodes to explore; sorted by estimated cost f(n) = g(n) + h(n)
    frontier = []

    # Dictionary to store the most efficient path
    came_from = {}

    # g holds the cost of the path from the start node to the current node
    g = {tuple(start): 0}

    # f is the estimated total cost from start to goal via the current node
    f = {tuple(start): permutation_transpositions_count(start, goal)}

    # Counter to track the number of developed nodes
    developed_nodes_count = 0

    # Push the initial state onto the priority queue with its f(n) value
    heapq.heappush(frontier, (f[tuple(start)], start))

    while frontier:
        # Pop the node with the lowest f(n) value from the priority queue
        _, current = heapq.heappop(frontier)

        # Goal check: if the current state matches the goal, reconstruct the path and return it
        if is_goal(current, goal):
            print("Quantity of nodes developed:", developed_nodes_count)
            return restore_path_for_astar_and_gbfs(came_from, start, goal, developed_nodes_count)

        # Expand neighbors of the current node
        for neighbor in get_neighbors(current):
            neighbor_tuple = tuple(neighbor)

            # g(current) + 1 represents the cost to reach the neighbor from the current node
            cost = g[tuple(current)] + 1

            # Only proceed if the neighbor hasn't been visited or a shorter path is found
            if neighbor_tuple not in g or cost < g[neighbor_tuple]:
                # Record the path to the neighbor
                came_from[neighbor_tuple] = tuple(current)

                # Update g and f costs for the neighbor
                g[neighbor_tuple] = cost
                h = permutation_transpositions_count(neighbor, goal)  # heuristic value for neighbor
                f[neighbor_tuple] = g[neighbor_tuple] + h

                # Add the neighbor to the priority queue with its f(n) value
                heapq.heappush(frontier, (f[neighbor_tuple], neighbor))

        # Increment the developed nodes counter
        developed_nodes_count += 1

    print("Quantity of nodes developed:", developed_nodes_count)
    # Return False if no solution was found
    return False
