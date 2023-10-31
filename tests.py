from slidey import Puzzle
# Init a test layout
# 1, 2, 3
# 0, 7, 5
# 8, 6, 4

test_puzzle = Puzzle([[1, 2, 3], [0, 7, 5], [8, 6, 4]])

# Checking 0-detection
test_puzzle.where_blank()

# Checking directions
test_puzzle.move('Up')
assert test_puzzle.state == [[0, 2, 3], [1, 7, 5], [8, 6, 4]], "Up Movement Error"

test_puzzle.move('Down')
assert test_puzzle.state == [[1, 2, 3], [0, 7, 5], [8, 6, 4]], "Down Movement Error"

test_puzzle.move('Right')
assert test_puzzle.state == [[1, 2, 3], [7, 0, 5], [8, 6, 4]], "Up Movement Error"

test_puzzle.move('Left')
assert test_puzzle.state == [[1, 2, 3], [0, 7, 5], [8, 6, 4]], "Up Movement Error"
