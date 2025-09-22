from dataclasses import dataclass


@dataclass
class Point:
    col: int
    row: int


directions = dict(
    n={'col': 0, 'row': -1}, s={'col': 0, 'row': 1},
    e={'col': 1, 'row': 0}, w={'col': -1, 'row': 0},
    ne={'col': 1, 'row': -1}, nw={'col': -1, 'row': -1},
    se={'col': 1, 'row': 1}, sw={'col': -1, 'row': 1},
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
            row + directions[direction]['row'], 
            col + directions[direction]['col']
            )
    