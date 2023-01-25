class Piece:

    def __init__(self, sort, color, position):
        if sort == "P":
            self.sort = sort
        elif sort == "K":
            raise AttributeError("invalid value, we are suppose that 'K' is defined by default")
        else:
            raise AttributeError("invalid value, sort must be 'K' or 'P' ")
        if color == "white" or color == "black":
            self.color = color
        else:
            raise AttributeError("invalid value, color must be 'black' or 'white' ")
        self.position = position


class Board:
    def __init__(self):
        self.position = dict()

    def add(self, piece):
        if piece.sort == "K" or piece.position in self.position:
            print("invalid query")
        else:
            self.position[piece.position] = piece

    def remove(self, position):
        if position in self.position:
            del self.position[position]
        else:
            print("invalid query")

    def move(self, piece, position2):
        if position2 not in self.position:
            piece.position = position2
            self.position[piece.position] = piece
        if position2 in self.position:
            if self.position[position2].color == piece.color:
                print("invalid query")
            else:
                if self.position[position2].sort == "K":
                    print("invalid query")
                else:
                    del self.position[position2]
                    del self.position[piece.position]
                    piece.position = position2
                    self.position[position2] = piece

    def is_mate(self, color):
        if color == "white":
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i != 0 or j != 0:
                        position = (i, i)
                        if position in self.position:
                            return True
            return False
        else:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i != 0 or j != 0:
                        if (i, i) in self.position:
                            return True
            return False

    def print(self, color):
        print(self.position)
        print(self.is_mate(color))


if __name__ == "__main__":
    board = Board()
    piece_1 = Piece(sort="P", color="black", position=(2, 10))
    piece_2 = Piece(sort="P", color="black", position=(-18, -4))
    piece_3 = Piece(sort="P", color="white", position=(5, 5))

    board.add(piece_1)
    board.add(piece_3)
    board.add(piece_2)
    board.remove(piece_3.position)
    board.remove((1, 1))
    board.remove((22, 33))
    board.move(piece=piece_1, position2=(5, 5))
    board.is_mate(piece_3.color)

    board.print(piece_3.color)
