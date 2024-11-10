from collections import deque

GOAL_STATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def is_goal(state):
    return state == GOAL_STATE

def get_neighbors(state):
    moves = []
    index = state.index(0)      
    directions = {'left': -1, 'right': 1, 'up': -3, 'down': 3}

    for direction, step in directions.items():
        new_index = index + step
        new_row, new_col = divmod(new_index, 3)
        
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = state[:]
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            moves.append(new_state)
    
    return moves


def getInvCount(arr):
    inv_count = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count
def isSolvable(puzzle) :
 
    # Count inversions in given 8 puzzle
    inv_count = getInvCount(puzzle)
 
    # return true if inversion count is even.
    return (inv_count % 2 == 0)

# BFS
def bfs(start):
    queue = deque([(start, [start])])
    visited = set()
    visited.add(tuple(start))
    developed_count = 0  
    
    while queue:
        state, path = queue.popleft()
        developed_count += 1  

        
        if is_goal(state):
            print("Total nodes developed:", developed_count)
            return path
        
        for neighbor in get_neighbors(state):
            if tuple(neighbor) not in visited:
                visited.add(tuple(neighbor))
                queue.append((neighbor, path + [neighbor]))
    
    print("Total nodes developed:", developed_count)
    return None  

def dls(state, path, depth, visited, developed_count):
    if depth == 0 and is_goal(state):
        return path, developed_count
    if depth > 0:
        for neighbor in get_neighbors(state):
            if tuple(neighbor) not in visited:
                visited.add(tuple(neighbor))
                developed_count += 1  # Increment the developed count for each node expanded
                result, developed_count = dls(neighbor, path + [neighbor], depth - 1, visited, developed_count)
                if result is not None:
                    return result, developed_count
                visited.remove(tuple(neighbor))  # Backtrack
    return None, developed_count

# Iterative Deepening Search (IDS) with developed count
def ids(start):
    depth = 0
    total_developed_count = 0  # Track total nodes developed across all depths
    while True:
        visited = set()
        visited.add(tuple(start))
        result, developed_count = dls(start, [start], depth, visited, 0)
        total_developed_count += developed_count  # Accumulate nodes developed at each depth
        if result is not None:
            print("Solution found at depth:", depth)
            print("Total nodes developed:", total_developed_count)
            return result
        depth += 1

# Main execution
def run_algorithms(start_state):
    print("BFS Path:", bfs(start_state))
    solution_path = ids(start_state)
    print("IDS path:", solution_path)


start_state = [1,2,0,3,4,5,6,7,8] 
print(isSolvable(start_state)) 
run_algorithms(start_state)
