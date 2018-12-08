from draughts.cobradraughts.core.DBoard import DBoard
from draughts.cobradraughts.core.DPiece import DPiece



def get_board():
    board = DBoard()
    board.light_pieces = []
    board.dark_pieces = []
    board.bitmap = [None] * 50
   

    # ajout des pions sur le damier


    row = 0
    column = 1
    delta = 1
    for _ in range(20): # nombre de pions noirs
        new_piece = DPiece(board, row, column, 'DARK')
        board.dark_pieces.append(new_piece)
        board.set_bitmap(row, column, new_piece)
        column += 2
        if column > 9:
            column -= (10 + delta)
            row += 1
            delta = -delta


    row = 6
    column = 1
    delta = 1
    for _ in range(20): # nombre de pions blancs
        new_piece = DPiece(board, row, column, 'LIGHT')
        board.light_pieces.append(new_piece)
        board.set_bitmap(row, column, new_piece)
        column += 2
        if column > 9:
            column -= (10 + delta)
            row += 1
            delta = -delta

    return board
