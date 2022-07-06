
board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '7h': 'bqueen', '3e': 'wking'}
c = [  '1a','2a','3a','4a','5a','6a','7a','8a',   
                '1b','2b','3b','4b','5b','6b','7b','8b', 
                '1c','2c','3c','4c','5c','6c','7c','8c', 
                '1d','2d','3d','4d','5d','6d','7d','8d', 
                '1e','2e','3e','4e','5e','6e','7e','8e', 
                '1f','2f','3f','4f','5f','6f','7f','8f', 
                '1g','2g','3g','4g','5g','6g','7g','8g', 
                '1h','2h','3h','4h','5h','6h','7h','8h'              ]
def isValidChessBoard(board):
    blackPieces= 0
    whitePieces= 0
    blackPawns = 0
    whitePawns = 0
    for piece in board.values():
        if (piece[0] == 'w'):
            whitePieces += 1
            print('number of whitePieces ' + (str(whitePieces)))
        else:
            blackPieces += 1
            print('number of blackPieces ' + (str(blackPieces)))
        if (piece == 'bpawn'):
            blackPawns += 1
            print('number of bpawns ' + (str(blackPawns)))
        if (piece == 'wpawn'):
            whitePawns += 1
            print('number of whitePawns ' + (str(whitePawns)))

    for place in board.keys():
        print(place)
        if (place not in c):
            return False

    if (blackPieces > 16 or whitePieces > 16 or blackPawns > 8 or whitePawns > 8):
        return False 

    return True


if isValidChessBoard(board):
    print('true')
else:
    print('false')


