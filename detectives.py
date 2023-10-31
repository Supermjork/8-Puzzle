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

init_puzzle = Puzzle([[1, 2, 3],
                      [4, 8, 5],
                      [7, 6, 0]])

solution = bfs(init_puzzle)

if solution:
    solved_puzzle, moves = solution
    print("Solution found!")
    for move in moves:
        print(move)
else:
    print("No solution found.")
