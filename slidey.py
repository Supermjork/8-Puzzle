# File containing Puzzle class

# Goal:
# 0 1 2
# 3 4 5
# 6 7 8
class Puzzle:
    goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    state = []

    def __init__(self, state):
        self.state = state

    def where_blank(self):
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == 0:
                    return (i, j)
        print("0 Not Found")

    def where_blank_gen(self):
        return [(i, j) for i in range(len(self.state)) for j in range(len(self.state[i])) if self.state[i][j] == 0]

test_puzzle = Puzzle([[1, 2, 3], [0, 7, 5], [8, 6, 4]])
