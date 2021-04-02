import numpy as np
import elements as el
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

dwarf_positions = [[0, 0], [1, 1], [7, 3], [2, 1]]
dwarf_pawns = []

el.fill_dwarf_pawn_list(dwarf_positions, dwarf_pawns, el.Dwarf)


class Board(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.board = np.chararray((15, 15), itemsize=2)
        for i in self.board:
            self.add_widget(Image(source='white_field.png'))

    def show(self):
        for i in range(225):
            self.add_widget(Image(source='white_field.png'))

    def print_board(self):
        print(self.board)

    def fill_board(self, pawns):
        for pawn in pawns:
            self.board[pawn['dwarf'].dim_x, pawn['dwarf'].dim_y] = pawn['id']


class ThudGame(BoxLayout):
    board = ObjectProperty(None)


class ThudApp(App):
    def build(self):
        return ThudGame()

        # board1 = Board()
        # eturn board1


if __name__ == '__main__':
    ThudApp().run()
'''
dwarf1 = el.Dwarf(5, 5)

board = Board()
board.show()
board.fill_board(dwarf_pawns)
board.show()
print(dwarf_pawns)
print(dwarf_pawns[0]['id'], dwarf_pawns[0]['dwarf'].dim_x)
print(len(dwarf_pawns))

print(type(dwarf1))
'''
