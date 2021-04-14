# Game elements module
from kivy.uix.button import Button

buffer = [0, 0]


def set_buffer(x, y):
    global buffer
    buffer[0] = x
    buffer[1] = y


def reset_buffer():
    global buffer
    buffer[0] = 0
    buffer[1] = 0


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
        self.name = self.text

    move_range = 15

    def on_press(self):
        if buffer == [0, 0]:
            set_buffer(self.pos[0], self.pos[1])
            self.text = str(self.move_range)
        else:
            self.pos[0] = buffer[0]
            self.pos[1] = buffer[1]
            reset_buffer()
            self.text = self.name


class Troll(Pawn):

    def __init__(self, dim_x, dim_y, text):
        super().__init__(dim_x, dim_y)
        self.text = 'T' + str(text)
        self.name = self.text

    def on_press(self):
        if buffer == [0, 0]:
            set_buffer(self.pos[0], self.pos[1])
            self.text = str(self.move_range)
        else:
            self.pos[0] = buffer[0]
            self.pos[1] = buffer[1]
            reset_buffer()
            self.text = self.name

    move_range = 1


def fill_pawn_list(positions, pawn_list, pawn_type):
    counter = 1
    for i in positions:
        pawn_list.append(
            pawn_type(i[0], i[1], counter)
        )
        counter += 1
