import sys


def is_valid_chess_board(user_input):
    notation_list = [y for x in user_input for y in x]
    squares, pieces, possible_pieces, count_king_white, count_king_black = [], [], ['K', 'B', 'R', 'Q', "N", "P"], 0, 0
    count_queen_white, count_queen_black, count_rook_white, count_rook_black = 0, 0, 0, 0
    count_knight_white, count_knight_black, count_bishop_white, count_bishop_black = 0, 0, 0, 0
    count_pawn_white, count_pawn_black, black_pieces, white_pieces = 0, 0, 0, 0

    for coordinates in notation_list:
        squares.append(coordinates[2:])
        pieces.append(coordinates[:2].upper())

    for square in squares:
        if square not in chess_board.keys():
            print(f'The coordinate "{square}" is invalid for a chess board.'), sys.exit()
        if chess_board[square] == "filled":
            print(f'The coordinate "{square}" is already filled.'), sys.exit()
        chess_board[square] = "filled"

    for piece in pieces:
        if piece not in possible_pieces:
            print("There is no such Chess piece."), sys.exit()

        if piece == "WK":
            count_king_white += 1
        elif piece == "BK":
            count_king_black += 1

        if piece == "WQ":
            count_queen_white += 1
        elif piece == "BQ":
            count_queen_black += 1

        if piece == "WR":
            count_rook_white += 1
        elif piece == "BR":
            count_rook_black += 1

        if piece == "WN":
            count_knight_white += 1
        elif piece == "BN":
            count_knight_black += 1

        if piece == "WB":
            count_bishop_white += 1
        elif piece == "BB":
            count_bishop_black += 1

        if piece == "WP":
            count_pawn_white += 1
        elif piece == "BP":
            count_pawn_black += 1

        if piece[0].lower() == "w":
            white_pieces += 1
        elif piece[0].lower() == "b":
            black_pieces += 1

    if (count_king_white or count_king_black) != 1:  # Checks the number of Kings is min & max 2 or not.
        print("White and Black must only have 1 king each."), sys.exit()
    if (count_queen_white or count_queen_black) > 1:  # Checks the number of Queens is max 2 or not.
        print("White and Black can only have maximum 1 queen each."), sys.exit()
    if (count_rook_white or count_rook_black) > 2:  # Checks the number of Rooks is max 2 or not.
        print("White and Black can only have maximum 2 rook each."), sys.exit()
    if (count_knight_white or count_knight_black) > 2:  # Checks the number of Knights is max 2 or not.
        print("White and Black can only have maximum 2 knights each."), sys.exit()
    if (count_bishop_white or count_bishop_black) > 2:  # Checks the number of Bishops is max 2 or not.
        print("White and Black can only have maximum 2 bishops each."), sys.exit()
    if (count_pawn_white or count_pawn_black) > 8:  # Checks the number of Pawns is max 2 or not.
        print("White and Black can only have maximum 8 pawns each."), sys.exit()
    if (white_pieces or black_pieces) > 16:  # Checks the total number of pieces on both sides is max or not.
        print("White and Black can only have maximum 16 pieces each."), sys.exit()
    return True


with open("in.txt", "r") as data:
    input_data = data.readlines()

chess_board = {
               "a8": "", "b8": "", "c8": "", "d8": "", "e8": "", "f8": "", "g8": "", "h8": "",
               "a7": "", "b7": "", "c7": "", "d7": "", "e7": "", "f7": "", "g7": "", "h7": "",
               "a6": "", "b6": "", "c6": "", "d6": "", "e6": "", "f6": "", "g6": "", "h6": "",
               "a5": "", "b5": "", "c5": "", "d5": "", "e5": "", "f5": "", "g5": "", "h5": "",
               "a4": "", "b4": "", "c4": "", "d4": "", "e4": "", "f4": "", "g4": "", "h4": "",
               "a3": "", "b3": "", "c3": "", "d3": "", "e3": "", "f3": "", "g3": "", "h3": "",
               "a2": "", "b2": "", "c2": "", "d2": "", "e2": "", "f2": "", "g2": "", "h2": "",
               "a1": "", "b1": "", "c1": "", "d1": "", "e1": "", "f1": "", "g1": "", "h1": ""
               }
end = True
input_data = [line.split() for line in input_data]
if is_valid_chess_board(input_data):
    print("Position is possible.")
