import numpy as np
import elements as el
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

board = np.empty((15, 15), dtype=el.Pawn)

dwarf_positions = [[0, 5], [0, 6], [0, 8], [0, 9], [1, 4], [1, 10],
                   [2, 3], [2, 11], [3, 2], [3, 12], [4, 1], [4, 13],
                   [5, 0], [5, 14], [6, 0], [6, 14], [8, 0], [8, 14],
                   [9, 0], [9, 14], [10, 1], [10, 13], [11, 2], [11, 12],
                   [12, 3], [12, 11], [13, 4], [13, 10], [14, 5], [14, 6],
                   [14, 8], [14, 9]]

troll_positions = [[6, 6], [6, 7], [6, 8], [7, 6],
                   [7, 8], [8, 6], [8, 7], [8, 8]]
pawn_list = []

empty_pawn = el.Pawn(0, 0)


class Board(GridLayout):

    el.fill_pawn_list(dwarf_positions, pawn_list, el.Dwarf)
    el.fill_pawn_list(troll_positions, pawn_list, el.Troll)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def fill_board(self, pawn_list):
        global board
        for pawn in pawn_list:
            board[pawn.dim_x, pawn.dim_y] = pawn

    def update_board(self):
        global board
        for index, i in np.ndenumerate(board):
            if i is None:
                self.add_widget(el.Field(0, 0))
            else:
                self.add_widget(i)


class ThudGame(BoxLayout):
    board = ObjectProperty(None)

    def set_board(self):
        self.board.fill_board(pawn_list)
        self.board.update_board()


class ThudApp(App):
    def build(self):
        game = ThudGame()
        game.set_board()
        return game


if __name__ == '__main__':
    ThudApp().run()


print(board)
