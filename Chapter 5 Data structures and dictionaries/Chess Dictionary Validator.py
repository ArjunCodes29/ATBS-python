board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
chessBoard = [  '1a','2a','3a','4a','5a','6a','7a','8a'    
                '1b','2b','3b','4b','5b','6b','7b','8b' 
                '1c','2c','3c','4c','5c','6c','7c','8c' 
                '1d','2d','3d','4d','5d','6d','7d','8d' 
                '1e','2e','3e','4e','5e','6e','7e','8e' 
                '1f','2f','3f','4f','5f','6f','7f','8f' 
                '1g','2g','3g','4g','5g','6g','7g','8g' 
                '1h','2h','3h','4h','5h','6h','7h','8h'              ]
def isValidChessBoard(board):
    blackPieces= 0
    whitePieces= 0
    blackPawns = 0
    whiePawns = 0
    for piece in board.values():
        if (piece[0] == 'w'):
            whitePieces += 1
        else:
            blackPieces += 1
        if (piece == 'bpawn'):
            blackPawns += 1
        if (piece == 'wpawn'):
            whiePawns += 1
    for place in board:
        if place not in chessBoard:
            return False
    if (blackPieces > 16 or whitePieces > 16 or blackPawns > 8 or whiePawns > 8):
        return False 

    return True

if isValidChessBoard(board):
    print('true')
else:
    print('false')
    
