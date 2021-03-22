import numpy as np
import elements as el
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

dwarf_positions = [[1, 1], [7, 3], [2, 1]]
dwarf_pawns = []

el.fill_pawn_list(dwarf_positions, dwarf_pawns, el.Dwarf)


class Board():
    def __init__(self):
        self.board = np.zeros((15, 15))

    def show(self):
        print(self.board)

    def fill_board(self, pawns):
        for pawn in pawns:
            self.board[pawn.dim_x, pawn.dim_y] = 'D'


class ThudGame(BoxLayout):
    pass


class ThudApp(App):
    def build(self):
        return ThudGame()


'''
if __name__ == '__main__':
    ThudApp().run()
'''

board = Board()
# board.show()
print(dwarf_pawns)
print(dwarf_pawns[0]['id'], dwarf_pawns[0]['dwarf'].dim_x)
print(len(dwarf_pawns))
