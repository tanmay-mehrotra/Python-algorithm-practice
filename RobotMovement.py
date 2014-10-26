'''
Created on Jun 25, 2014
@author: tanmaymehrotra
'''

def findPath(board,x,y):
    if x > 3 or y > 3:
        return False
    if board[x][y] == 1:
        return False
    if x == 3 and y == 3:
        return True
    if not (findPath(board, x, y+1) or findPath(board,x+1,y)):
        return False
    else:
        return True
    
def findPathUsingDP(board,x,y):
    if x > 3 or y > 3:
        return False
    if board[x][y] == 1:
        return False
    if x == 3 and y == 3:
        return True
    if not (findPath(board, x, y+1) or findPath(board,x+1,y)):
        board[x][y] = 1
        return False
    else:
        return True
    
if __name__ == '__main__':
    board = [[0,0,0,1],[0,1,0,0],[0,0,1,0],[0,0,1,0]]
    print findPathUsingDP(board, 0, 0)
    #print findPath(board, 0, 0)
    print board
    