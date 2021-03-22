# Game elements module

class Pawn():
    def __init__(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y

    def __str__(self):
        return 'dwarf: [{},{}]'.format(self.dim_x, self.dim_y)

    def move(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y


class Dwarf(Pawn):
    symbol = "D"
    is_dwarf = True
    pass


class Troll(Pawn):
    symbol = "T"
    is_troll = True
    pass


def fill_pawn_list(positions, pawn_list, pawn_type):
    counter = 0
    for i in positions:
        pawn_list.append({
            'id': pawn_type.symbol + str(counter),
            'dwarf': pawn_type(i[0], i[1])
        })
        counter += 1
