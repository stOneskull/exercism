directions = {
    "north": {'x': 0, 'y': -1},
    "east": {'x': 1, 'y': 0},
    "south": {'x': 0, 'y': 1},
    "west": {'x': -1, 'y': 0},
    "northeast": {'x': 1, 'y': -1},
    'southeast': {"x": 1, "y": 1},
    "southwest": {'x': -1, 'y': 1},
    "northwest": {'x': -1, 'y': -1},
}


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    

class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        for row in range(len(self.puzzle)):
            for col in range(len(self.puzzle[row])):
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
        if row >= len(self.puzzle) or col >= len(self.puzzle[row]):
            return False
        if self.puzzle[row][col] != word[0]:
            return False
        
        self.end = Point(col, row)
        return self.hunt(
            word[1:], direction,
            row + directions[direction]['x'], 
            col + directions[direction]['y']
            )
    