# Game elements module
from kivy.uix.button import Button


class Pawn(Button):

    def __init__(self, dim_x, dim_y):
        super().__init__()
        self.dim_x = dim_x
        self.dim_y = dim_y

    def move(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y


class Dwarf(Pawn):

    def __init__(self, dim_x, dim_y, text):
        super().__init__(dim_x, dim_y)
        self.text = 'D' + str(text)

    move_range = 15


class Troll(Pawn):

    def __init__(self, dim_x, dim_y, text):
        super().__init__(dim_x, dim_y)
        self.text = 'T' + str(text)

    move_range = 1


def fill_pawn_list(positions, pawn_list, pawn_type):
    counter = 1
    for i in positions:
        pawn_list.append(
            pawn_type(i[0], i[1], counter)
        )
        counter += 1
