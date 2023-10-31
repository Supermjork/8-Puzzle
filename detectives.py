from slidey import Puzzle

# Implementing the 2 searching algorithms of choice
# BFS
def bfs(states: list[Puzzle]):
    generated_states = []

    for state in states:
        moves = state.legal_moves()

        for move in moves:
            generated_states.append(state.create_child().move(move))

    for state in generated_states:
        if state.state == state.goal:
            return state
        
    bfs(generated_states)
    pass

# DFS

init_puzzle = [Puzzle([[1, 2, 3], [4, 0, 5], [7, 8, 6]])]

print(bfs(init_puzzle))
