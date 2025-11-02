#r=rook h=horse/knight b=bishop q=queen k=king e=empty
#lowercase=black uppercase=white
startboard=[['r','h','b','q','k','b','h','r'],
         ['p','p','p','p','p','p','p','p'],
         ['e','e','e','e','e','e','e','e'],
         ['e','e','e','e','e','e','e','e'],
         ['e','e','e','e','e','e','e','e'],
         ['e','e','e','e','e','e','e','e'],
         ['P','P','P','P','P','P','P','P'],
         ['R','H','B','Q','K','B','H','R']]


def getValidMoves(board, position):
    #TODO: handle pinned pieces
    row, col =position
    piece=board[row][col]
    valid_moves=[]
    if piece=='e':
        return valid_moves
    if piece=='P':
        if board[row-1][col]=='e':#move once
            valid_moves.append([row-1,col])
        if row==6:
            if board[row-2][col]=='e':
                valid_moves.append([row-2,col])
        #captures
        if col==0:#avoid out of bounds index
            if board[row-1][col+1].islower() and board[row-1][col+1]!='e':
                valid_moves.append([row-1,col+1])
        if col==7:#avoid out of bounds index
            if board[row-1][col-1].islower() and board[row-1][col-1]!='e':
                valid_moves.append([row-1,col-1])
        if col>0 and col<7:
            if board[row-1][col+1].islower() and board[row-1][col+1]!='e':
                valid_moves.append([row-1,col+1])
            if board[row-1][col-1].islower() and  board[row-1][col-1]!='e':
                valid_moves.append([row-1,col-1])
    if piece=='p':
        if board[row+1][col]=='e':#move once
            valid_moves.append([row+1,col])
        if row==1:
            if board[row+2][col]=='e':
                valid_moves.append([row+2,col])
        #captures
        if col==0:#avoid out of bounds index
            if board[row+1][col+1].islower() and board[row+1][col+1]!='e':
                valid_moves.append([row+1,col+1])
        if col==7:#avoid out of bounds index
            if board[row+1][col-1].islower() and board[row+1][col-1]!='e':
                valid_moves.append([row+1,col-1])
        if col>0 and col<7:
            if board[row+1][col+1].islower() and board[row+1][col+1]!='e':
                valid_moves.append([row+1,col+1])
            if board[row+1][col-1].islower() and  board[row+1][col-1]!='e':
                valid_moves.append([row+1,col-1])
    if piece=='h' or piece=='H':
        possible_moves=[
            [row-1,col-2],[row-2,col-1],[row-2,col+1],[row-1,col+2],[row+1,col+2],[row+2,col+1],[row+2,col-1],[row+1,col-2]
            ]
        for move in possible_moves:
            hrow, hcol=move
            if inbounds(move):
                if (board[hrow,hcol]=='e' or (board[hrow,hcol].islower() and piece=='H') or (board[hrow,hcol].isupper() and piece=='h')):
                    valid_moves.append(move)
  #  if piece=='r' or piece=='R':
        
                    
def pinned(board, piece):
    #TODO
    return True

def inbounds(position):
    row,col=position
    if row>=0 and row<=7 and col>=0 and col<=7:
        return True