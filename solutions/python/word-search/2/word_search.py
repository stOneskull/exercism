from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


directions = dict(
    n={'x': 0, 'y': -1}, s={'x': 0, 'y': 1},
    e={'x': 1, 'y': 0}, w={'x': -1, 'y': 0},
    ne={'x': 1, 'y': -1}, nw={'x': -1, 'y': -1},
    se={'x': 1, 'y': 1}, sw={'x': -1, 'y': 1},
)


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.rows = len(puzzle)
        self.cols = len(puzzle[0])

    def search(self, word):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.puzzle[row][col] == word[0]:
                    start = Point(col, row)
                    for direction in directions:
                        if self.hunt(word, direction, row, col):
                            return ((start, self.end))

    def hunt(self, word, direction, row, col):
        if word == "":
            return True
        
        if row < 0 or col < 0:
            return False
        if row >= self.rows or col >= self.cols:
            return False
        if self.puzzle[row][col] != word[0]:
            return False
        
        self.end = Point(col, row)
        return self.hunt(
            word[1:], direction,
            row + directions[direction]['x'], 
            col + directions[direction]['y']
            )
    