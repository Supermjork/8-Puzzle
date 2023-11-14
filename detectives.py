from slidey import Puzzle
from typing import Optional, Tuple
from collections import deque

# Implementing the 2 searching algorithms of choice
# BFS
def bfs(start: Puzzle) -> Optional[Tuple[Puzzle, list[str]]]:
    queue = deque([(start, [])])
    visited = set([str(start)])

    while queue:
        current_puzzle, path = queue.popleft()

        if current_puzzle.state == current_puzzle.goal:
            return current_puzzle, path

        legal_moves = current_puzzle.legal_moves()
        for move in legal_moves:
            child_puzzle = current_puzzle.create_child()
            child_puzzle.move(move)

            if str(child_puzzle) not in visited:
                queue.append((child_puzzle, path + [move]))
                visited.add(str(child_puzzle))

    return None

# DFS
def dfs(start: Puzzle) -> Optional[Tuple[Puzzle, list[str]]]:
    stack = [(start, [])]
    visited = set([str(start)])

    while stack:
        current_puzzle, path = stack.pop()

        if current_puzzle.state == current_puzzle.goal:
            return current_puzzle, path

        legal_moves = current_puzzle.legal_moves()
        for move in legal_moves:
            child_puzzle = current_puzzle.create_child()
            child_puzzle.move(move)

            if str(child_puzzle) not in visited:
                stack.append((child_puzzle, path + [move]))
                visited.add(str(child_puzzle))

    return None

# Implement A*, Greedy, Uniform

init_puzzle = Puzzle([[1, 2, 3],
                      [4, 0, 5],
                      [7, 8, 6]
                    ])

solution_bfs = bfs(init_puzzle)

if solution_bfs:
    solved_puzzle, moves = solution_bfs
    print("Solution found!")
    for move in moves:
        print(move)
else:
    print("No solution found.")

solution_dfs = dfs(init_puzzle)

if solution_dfs:
    solved_puzzle, moves = solution_dfs
    print("Solution found!")
    for move in moves:
        print(move)
else:
    print("No solution found.")
