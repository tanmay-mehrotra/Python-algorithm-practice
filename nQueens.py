'''
Created on Jun 21, 2014
@author: tanmaymehrotra
'''

def nQueens(board,row):
    if row>len(board)-1:
        print board
        return
    for col in range(len(board)):
        if canPlace(board, col, row):
            board[row]=col
            nQueens(board, row+1)
                
            
def canPlace(board, x, y):
    for row in range(y):
        if board[row] == x or abs(row - y) == abs(board[row] - x):
            return False
    return True
    
if __name__ == '__main__':
    board = [0,0,0,0]
    nQueens(board,0)