BLACK, WHITE, NONE = "B", "W", ""


class Board:
    def __init__(self, board):
        self.height = len(board)
        self.width = len(board[0])
        self.grid = {
            (col, row): board[row][col]
            for row in range(self.height)
            for col in range(self.width)
        }

    def territory(self, x, y):
        if x not in range(self.width) or y not in range(self.height):
            raise ValueError("Invalid coordinate")

        if self.grid[(x, y)] != " ":
            return (NONE, set())

        terra = set()
        borders = set()
        to_visit = [(x, y)]
        visited = {(x, y)}

        while to_visit:
            current_x, current_y = to_visit.pop()

            if self.grid[(current_x, current_y)] == " ":
                terra.add((current_x, current_y))

                neighbors = [
                    (current_x - 1, current_y),
                    (current_x + 1, current_y),
                    (current_x, current_y - 1),
                    (current_x, current_y + 1),
                ]

                for neighbor_x, neighbor_y in neighbors:
                    if (
                        (neighbor_x, neighbor_y) not in visited
                        and neighbor_x in range(self.width)
                        and neighbor_y in range(self.height)
                    ):
                        visited.add((neighbor_x, neighbor_y))
                        to_visit.append((neighbor_x, neighbor_y))
            else:
                borders.add(self.grid[(current_x, current_y)])

        owner = NONE if len(borders) != 1 else borders.pop()
        return (owner, terra)


    def territories(self):
        terra = {BLACK: set(), WHITE: set(), NONE: set()}

        for y in range(self.height):
            for x in range(self.width):
                if self.grid[(x, y)] == " ":
                    owner, found_territory = self.territory(x, y)
                    terra[owner].update(found_territory)

        return terra
