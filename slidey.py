# File containing Puzzle class

# Goal:
# 0 1 2
# 3 4 5
# 6 7 8

from copy import deepcopy

class Puzzle:
    goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    state = []
    prev_states = []
    moves = 0

    def __init__(self, state: list, goal: list[list[int]] = [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
                 prev_states: list = [], moves: int = 0):
        self.state = state
        self.goal = goal
        self.prev_states = prev_states
        self.moves = moves

    def where_blank(self):
        return [(i, j) for i in range(len(self.state)) for j in range(len(self.state[i])) if self.state[i][j] == 0]
    
    def legal_moves(self):
        blank_Y, blank_X = self.where_blank()[0]

        legal = ['Up', 'Down', 'Left', 'Right']

        if blank_Y == 0:
            # Can go: Left, Down, Right
            legal.remove('Up')
        elif blank_Y == len(self.state):
            # Can go: Left, Up, Right
            legal.remove('Down')
        
        if blank_X == 0:
            # Can go: Up, Down, Right
            legal.remove('Left')
        elif blank_X == len(self.state[0]):
            legal.remove('Right')

        return legal
    
    def move(self, move: str):
        blank_Y, blank_X = self.where_blank()[0]

        self.prev_states.append(self.state)

        if move == 'Up':
            self.state[blank_Y][blank_X], self.state[blank_Y - 1][blank_X] = self.state[blank_Y - 1][blank_X], 0
        elif move == 'Down':
            self.state[blank_Y][blank_X], self.state[blank_Y + 1][blank_X] = self.state[blank_Y + 1][blank_X], 0
        elif move == 'Left':
            self.state[blank_Y][blank_X], self.state[blank_Y][blank_X - 1] = self.state[blank_Y][blank_X - 1], 0
        elif move == 'Right':
            self.state[blank_Y][blank_X], self.state[blank_Y][blank_X + 1] = self.state[blank_Y][blank_X + 1], 0
        else:
            print("Outta luck buckaroo")

        self.moves += 1

        return self
    
    def validate_seq(self):
        sequence = [*range(len(self.state) ** 2)]

        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] in sequence:
                    sequence.remove(self.state[i][j])
        
        if len(sequence) == 0:
            return True
        else:
            return False
        
    def print_prev(self):
        for state in self.prev_states:
            print(state)
    
    def __str__(self):
        return str('\n'.join([', '.join([str(cell) for cell in row]) for row in self.state]))

    def create_child(self):
            child = deepcopy(self)
            child.prev_states.append(self.state)
            return child

# Init a test layout
# 1, 2, 3
# 0, 7, 5
# 8, 6, 4

test_puzzle = Puzzle([[1, 2, 3], [0, 7, 5], [8, 6, 4]])

print(f"Moves Done: {test_puzzle.moves}")
print(f"Validity of Sequence: {test_puzzle.validate_seq()}")
print(test_puzzle.where_blank())
print(test_puzzle.legal_moves())
print(test_puzzle.move('Down'))
print(f"Moves Done: {test_puzzle.moves}")

print("-------------------------------")

print("Child Creation")
child = test_puzzle.create_child()

print(f"Child Move Count: {child.moves}")
print(f"Making child move Right:\n{child.move('Right')}")
print(f"Child Move Count After move: {child.moves}")
print(f"Parent Move Count: {test_puzzle.moves}")

print(f"Comparing Child to Parent's state:\n{child.state}\n\n{test_puzzle.state}\n")

print(f"Child Previous States: \n{child.print_prev()}\n")

print(f"Parent Previous States: \n{test_puzzle.print_prev()}")
