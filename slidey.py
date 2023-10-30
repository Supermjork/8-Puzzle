# File containing Puzzle class

# Goal:
# 0 1 2
# 3 4 5
# 6 7 8

class Puzzle:
    goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    state = []

    def __init__(self, state: list[list[int]]):
        self.state = state

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


# Init a test layout
# 1, 2, 3
# 0, 7, 5
# 8, 6, 4

test_puzzle = Puzzle([[1, 2, 3], [0, 7, 5], [8, 6, 4]])

print(test_puzzle.where_blank())
print(test_puzzle.legal_moves())