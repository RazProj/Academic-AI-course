import argparse
from utils import is_solvable
from iddfs import iddfs
from bfs import bfs
from Astar import a_star
from gbfs import gbfs

GOAL_STATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def run_algorithms(start_state):
    print("Running algorithm BFS...")
    bfs_path = bfs(start_state, GOAL_STATE)
    print("Path:", bfs_path if bfs_path else "No solution found.")
    print()

    print("Running algorithm IDDFS...")
    solution_path = iddfs(start_state, GOAL_STATE)
    print("Path:", solution_path if solution_path else "No solution found.")
    print()

    print("Running algorithm A*...")
    solution, developed_nodes = a_star(start_state, GOAL_STATE)
    print("Path:", solution if solution else "No solution found.")
    print()

    print("Running algorithm Greedy Best-First Search...")
    solution, developed_nodes = gbfs(start_state, GOAL_STATE)
    print("Path:", solution if solution else "No solution found.")
    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_state", nargs=9, type=int)
    args = parser.parse_args()

    input_state = args.input_state

    # Checks the parity of the quantity of the inversions.
    if is_solvable(input_state):
        run_algorithms(input_state)
    else:
        print("The puzzle is not solvable.")
