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


class Field(Button):

    def __init__(self, dim_x, dim_y):
        super().__init__(background_color=(100, 1, 1, 1))
        self.dim_x = dim_x
        self.dim_y = dim_y

    def on_press(self):
        if self.text == '':
            self.text = str(self.dim_x) + ', ' + str(self.dim_y)
        else:
            self.text = ''


BufferPawn = Field(0, 0)


def set_BufferPawn(x, y):
    global BufferPawn
    BufferPawn.dim_x = x
    BufferPawn.dim_y = y


def reset_BufferPawn():
    global BufferPawn
    BufferPawn.dim_x = 0
    BufferPawn.dim_y = 0


class Pawn(Button):

    def __init__(self, dim_x, dim_y):
        super().__init__()
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.is_clicked = False

    def move(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y

    def on_press(self):
        global buffer
        global board
        x = y = 0
        if buffer[0] == 0 and buffer[1] == 0:
            buffer[0] = self.pos[0]
            buffer[1] = self.pos[1]
            self.text = str(buffer[0]) + ' , ' + str(buffer[1])
        elif buffer[0] == self.pos[0] and buffer[1] == self.pos[1]:
            self.text = str(self.name)
            reset_buffer()
        elif 'D' in self.name:
            self.text = 'kust'
            reset_BufferPawn()


class Dwarf(Pawn):

    def __init__(self, dim_x, dim_y, text):
        super().__init__(dim_x, dim_y)
        self.background_color = (1, 1, 100, 1)
        self.text = 'D' + str(text)
        self.name = self.text

    move_range = 15


class Troll(Pawn):

    def __init__(self, dim_x, dim_y, text):
        super().__init__(dim_x, dim_y)
        self.background_color = (1, 100, 1, 1)
        self.text = 'T' + str(text)
        self.name = self.text

    move_range = 1


def fill_pawn_list(positions, pawn_list, pawn_type):
    counter = 1
    for i in positions:
        pawn_list.append(
            pawn_type(i[0], i[1], counter)
        )
        counter += 1


# if eveliable_move() =
# po kliknięciu jeśli button nie jest pionkiem -> podświetlenie
