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

endgame=[['e','e','e','e','k','e','e','e'],
         ['e','e','B','e','e','e','e','e'],
         ['e','e','e','e','e','e','q','e'],
         ['e','r','e','e','e','e','e','e'],
         ['R','e','e','e','H','e','e','e'],
         ['e','e','e','e','e','e','e','e'],
         ['e','e','Q','e','e','e','b','e'],
         ['h','e','e','e','K','e','e','e']]
def getValidMoves(board, position):
    #TODO: handle pinned pieces
    row=position[0]
    col=position[1]
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
          #  hrow, hcol=move
            hrow=move[0]
            hcol=move[1]
            if inbounds(move):
                if (board[hrow][hcol]=='e' or (board[hrow][hcol].islower() and piece=='H') or (board[hrow][hcol].isupper() and piece=='h')):
                    valid_moves.append(move)
    if piece=='r' or piece=='R':
        #check all four directions
        condition=True
        i=1
        while condition:
            if inbounds([row+i,col]):
                if board[row+i][col]!='e':
                    if piece=='r':
                        if board[row+i][col].isupper():
                            valid_moves.append([row+i,col])
                        condition=False#if a piece is found, rook cannot move further (either black or white)
                    else:
                        if board[row+i][col].islower():
                            valid_moves.append([row+i,col])
                        condition=False
                else:
                    valid_moves.append([row+i,col])
                    i+=1
            else:
                condition=False
        
        condition=True
        i=1
        while condition:
            if inbounds([row-i,col]):
                if board[row-i][col]!='e':
                    if piece=='r':
                        if board[row-i][col].isupper():
                            valid_moves.append([row-i,col])
                        condition=False
                    else:
                        if board[row-i][col].islower():
                            valid_moves.append([row-i,col])
                        condition=False
                else:
                    valid_moves.append([row-i,col])
                    i+=1
            else:
                condition=False
        
        condition=True
        i=1
        while condition:
            if inbounds([row,col+i]):
                if board[row][col+i]!='e':
                    if piece=='r':
                        if board[row][col+i].isupper():
                            valid_moves.append([row,col+i])
                        condition=False
                    else:
                        if board[row][col+i].islower():
                            valid_moves.append([row,col+i])
                        condition=False
                else:
                    valid_moves.append([row,col+i])
                    i+=1
            else:
                condition=False
                
                
        condition=True
        i=1
        while condition:
            if inbounds([row,col-i]):
                if board[row][col-i]!='e':
                    if piece=='r':
                        if board[row][col-i].isupper():
                            valid_moves.append([row,col-i])
                        condition=False
                    else:
                        if board[row][col-i].islower():
                            valid_moves.append([row,col-i])
                        condition=False
                else:
                    valid_moves.append([row,col-i])
                    i+=1
            else:
                condition=False
    
    
    if piece=='b' or piece=='B':
        #check all four directions
        condition=True
        i=1
        while condition:
            if inbounds([row+i,col+i]):
                if board[row+i][col+i]!='e':
                    if piece=='b':
                        if board[row+i][col+i].isupper():
                            valid_moves.append([row+i,col+i])
                        condition=False#if a piece is found, bishop cannot move further (either black or white)
                    else:
                        if board[row+i][col+i].islower():
                            valid_moves.append([row+i,col+i])
                        condition=False
                else:
                    valid_moves.append([row+i,col+i])
                    i+=1
            else:
                condition=False
        
        condition=True
        i=1
        while condition:
            if inbounds([row-i,col+i]):
                if board[row-i][col+i]!='e':
                    if piece=='b':
                        if board[row-i][col+i].isupper():
                            valid_moves.append([row-i,col+i])
                        condition=False
                    else:
                        if board[row-i][col+i].islower():
                            valid_moves.append([row-i,col+i])
                        condition=False
                else:
                    valid_moves.append([row-i,col+i])
                    i+=1
            else:
                condition=False
        
        condition=True
        i=1
        while condition:
            if inbounds([row-i,col-i]):
                if board[row-i][col-i]!='e':
                    if piece=='b':
                        if board[row-i][col-i].isupper():
                            valid_moves.append([row-i,col-i])
                        condition=False
                    else:
                        if board[row-i][col-i].islower():
                            valid_moves.append([row-i,col-i])
                        condition=False
                else:
                    valid_moves.append([row-i,col-i])
                    i+=1
            else:
                condition=False
                
                
        condition=True
        i=1
        while condition:
            if inbounds([row+i,col-i]):
                if board[row+i][col-i]!='e':
                    if piece=='b':
                        if board[row+i][col-i].isupper():
                            valid_moves.append([row+i,col-i])
                        condition=False
                    else:
                        if board[row+i][col-i].islower():
                            valid_moves.append([row+i,col-i])
                        condition=False
                else:
                    valid_moves.append([row+i,col-i])
                    i+=1
            else:
                condition=False
    if piece=='q' or piece=='Q':
        valid_moves.extend(queenmoves(board,position))
    if piece=='k' or piece=='K':
        valid_moves.extend(kingmoves(board,position))
    
    
    return valid_moves
                    
def pinned(board, piece):
    #TODO
    return True

def inbounds(position):
    row=position[0]
    col=position[1]
    if row>=0 and row<=7 and col>=0 and col<=7:
        return True
    return False
    
def queenmoves(board, position):#copy pasted logic of rook+bishop
    row=position[0]
    col=position[1]
    piece=board[row][col]
    condition=True
    i=1
    valid_moves=[]
    while condition:
        if inbounds([row+i,col]):
            if board[row+i][col]!='e':
                if piece=='q':
                    if board[row+i][col].isupper():
                        valid_moves.append([row+i,col])
                    condition=False
                else:
                    if board[row+i][col].islower():
                        valid_moves.append([row+i,col])
                    condition=False
            else:
                valid_moves.append([row+i,col])
                i+=1
        else:
            condition=False
    
    condition=True
    i=1
    while condition:
        if inbounds([row-i,col]):
            if board[row-i][col]!='e':
                if piece=='q':
                    if board[row-i][col].isupper():
                        valid_moves.append([row-i,col])
                    condition=False
                else:
                    if board[row-i][col].islower():
                        valid_moves.append([row-i,col])
                    condition=False
            else:
                valid_moves.append([row-i,col])
                i+=1
        else:
            condition=False
    
    condition=True
    i=1
    while condition:
        if inbounds([row,col+i]):
            if board[row][col+i]!='e':
                if piece=='q':
                    if board[row][col+i].isupper():
                        valid_moves.append([row,col+i])
                    condition=False
                else:
                    if board[row][col+i].islower():
                        valid_moves.append([row,col+i])
                    condition=False
            else:
                valid_moves.append([row,col+i])
                i+=1
        else:
            condition=False
            
            
    condition=True
    i=1
    while condition:
        if inbounds([row,col-i]):
            if board[row][col-i]!='e':
                if piece=='q':
                    if board[row][col-i].isupper():
                        valid_moves.append([row,col-i])
                    condition=False
                else:
                    if board[row][col-i].islower():
                        valid_moves.append([row,col-i])
                    condition=False
            else:
                valid_moves.append([row,col-i])
                i+=1
        else:
            condition=False
    condition=True
    i=1
    while condition:
         if inbounds([row+i,col+i]):
             if board[row+i][col+i]!='e':
                 if piece=='q':
                     if board[row+i][col+i].isupper():
                         valid_moves.append([row+i,col+i])
                     condition=False
                 else:
                     if board[row+i][col+i].islower():
                         valid_moves.append([row+i,col+i])
                     condition=False
             else:
                 valid_moves.append([row+i,col+i])
                 i+=1
         else:
             condition=False
     
    condition=True
    i=1
    while condition:
         if inbounds([row-i,col+i]):
             if board[row-i][col+i]!='e':
                 if piece=='q':
                     if board[row-i][col+i].isupper():
                         valid_moves.append([row-i,col+i])
                     condition=False
                 else:
                     if board[row-i][col+i].islower():
                         valid_moves.append([row-i,col+i])
                     condition=False
             else:
                 valid_moves.append([row-i,col+i])
                 i+=1
         else:
             condition=False
     
    condition=True
    i=1
    while condition:
         if inbounds([row-i,col-i]):
             if board[row-i][col-i]!='e':
                 if piece=='q':
                     if board[row-i][col-i].isupper():
                         valid_moves.append([row-i,col-i])
                     condition=False
                 else:
                     if board[row-i][col-i].islower():
                         valid_moves.append([row-i,col-i])
                     condition=False
             else:
                 valid_moves.append([row-i,col-i])
                 i+=1
         else:
             condition=False
             
             
    condition=True
    i=1
    while condition:
         if inbounds([row+i,col-i]):
             if board[row+i][col-i]!='e':
                 if piece=='q':
                     if board[row+i][col-i].isupper():
                         valid_moves.append([row+i,col-i])
                     condition=False
                 else:
                     if board[row+i][col-i].islower():
                         valid_moves.append([row+i,col-i])
                     condition=False
             else:
                 valid_moves.append([row+i,col-i])
                 i+=1
         else:
             condition=False
    return valid_moves

#same logic as queen. but only moves 1 tile and cannot move to a tile that is under attack
def kingmoves(board,position):
    row=position[0]
    col=position[1]
    piece=board[row][col]
    i=1
    valid_moves=[]
    if inbounds([row+i,col]):
        if not underAttack(board,[row+i,col],position):
            if board[row+i][col]!='e':
                if piece=='k':
                    if board[row+i][col].isupper():
                        valid_moves.append([row+i,col])
                else:
                    if board[row+i][col].islower():
                        valid_moves.append([row+i,col])
            else:
                valid_moves.append([row+i,col])
                i+=1
    
    i=1
    if inbounds([row-i,col]):
        if not underAttack(board,[row-i,col],position):
            if board[row-i][col]!='e':
                if piece=='k':
                    if board[row-i][col].isupper():
                        valid_moves.append([row-i,col])
                else:
                    if board[row-i][col].islower():
                        valid_moves.append([row-i,col])
            else:
                valid_moves.append([row-i,col])
                i+=1    
    i=1
    if inbounds([row,col+i]):
        if not underAttack(board,[row,col+i],position):
            if board[row][col+i]!='e':
                if piece=='k':
                    if board[row][col+i].isupper():
                        valid_moves.append([row,col+i])
                else:
                    if board[row][col+i].islower():
                        valid_moves.append([row,col+i])
            else:
                valid_moves.append([row,col+i])
                i+=1           
            
    i=1
    if inbounds([row,col-i]):
        if not underAttack(board,[row,col-i],position):
            if board[row][col-i]!='e':
                if piece=='k':
                    if board[row][col-i].isupper():
                        valid_moves.append([row,col-i])
                else:
                    if board[row][col-i].islower():
                        valid_moves.append([row,col-i])
            else:
                valid_moves.append([row,col-i])
                i+=1
    i=1
    if inbounds([row+i,col+i]):
        if not underAttack(board,[row+i,col+i],position):
             if board[row+i][col+i]!='e':
                 if piece=='k':
                     if board[row+i][col+i].isupper():
                         valid_moves.append([row+i,col+i])
                 else:
                     if board[row+i][col+i].islower():
                         valid_moves.append([row+i,col+i])
             else:
                 valid_moves.append([row+i,col+i])
                 i+=1
     
    i=1
    if inbounds([row-i,col+i]):
        if not underAttack(board,[row-i,col+i],position):
             if board[row-i][col+i]!='e':
                 if piece=='k':
                     if board[row-i][col+i].isupper():
                         valid_moves.append([row-i,col+i])
                 else:
                     if board[row-i][col+i].islower():
                         valid_moves.append([row-i,col+i])
             else:
                 valid_moves.append([row-i,col+i])
                 i+=1

     
    i=1
    if inbounds([row-i,col-i]):
        if not underAttack(board,[row-i,col-i],position):
             if board[row-i][col-i]!='e':
                 if piece=='k':
                     if board[row-i][col-i].isupper():
                         valid_moves.append([row-i,col-i])
                 else:
                     if board[row-i][col-i].islower():
                         valid_moves.append([row-i,col-i])
             else:
                 valid_moves.append([row-i,col-i])
                 i+=1
             
             
    i=1
    if inbounds([row+i,col-i]):
        if not underAttack(board,[row+i,col-i],position):
             if board[row+i][col-i]!='e':
                 if piece=='k':
                     if board[row+i][col-i].isupper():
                         valid_moves.append([row+i,col-i])
                 else:
                     if board[row+i][col-i].islower():
                         valid_moves.append([row+i,col-i])
             else:
                 valid_moves.append([row+i,col-i])
                 i+=1
    return valid_moves


def underAttack(board,position,origin):#use origin position to check piece color
    orrow=origin[0]
    orcol=origin[1]
    if board[orrow][orcol].isupper():
        white=1
    else:
        white=0
    row=position[0]
    col=position[1]
    for i in range(8):
        for j in range(8):
            if board[i][j]!='e':
                if white==1:
                    if board[i][j].islower():
                        if board[i][j]!='k' and board[i][j]!='K':
                            if position in getValidMoves(board, [i,j]):
                                return True
                else:
                    if board[i][j].isupper():
                        if board[i][j]!='k' and board[i][j]!='K':
                            if position in getValidMoves(board, [i,j]):
                                return True
    return False#if no enemy piece is found which is attacking position, it is not under attack