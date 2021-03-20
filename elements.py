# Game elements module

class Pawn():
    def __init__(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y

    def move(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y


class Dwarf(Pawn):
    pass


class Troll(Pawn):
    moveRange = 1
    pass
