class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")
        if row > 7:
            raise ValueError("row not on board")

        self.row = row
        self.column = column

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def can_attack(self, other):
        if self == other:
            raise ValueError("Invalid queen position: both queens in the same square")

        return (
            self.row == other.row
            or self.column == other.column
            or abs(self.row - other.row) == abs(self.column - other.column)
        )
