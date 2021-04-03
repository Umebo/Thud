# Game elements module
from kivy.uix.button import Button


class Pawn(Button):

    def __str__(self):
        return '{}: [{},{}]'.format(self.symbol, self.dim_x, self.dim_y)

    def move(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y


class Dwarf(Pawn):

    def __init__(self, dim_x, dim_y, symbol):
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.symbol = symbol

    symbol = "D"
    move_range = 15
    is_dwarf = True
    pass


class Troll(Pawn):

    def __init__(self, dim_x, dim_y, symbol):
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.symbol = symbol

    symbol = "T"
    move_range = 1
    is_troll = True
    pass


def fill_pawn_list(positions, pawn_list, pawn_type):
    counter = 1
    for i in positions:
        pawn_list.append(
            pawn_type(i[0], i[1], pawn_type.symbol + str(counter))
        )
        counter += 1
