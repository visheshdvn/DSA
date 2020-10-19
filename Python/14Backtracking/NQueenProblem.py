# N-Queens
# Send Feedback
# You are given N, and for a given N x N chessboard, find a way to place N queens such that no queen can attack any other queen on the chess board.
# A queen can be killed when it lies in the same row, or same column, or the same diagonal of any of the other queens. You have to print all such configurations.
# Input Format :
# Line 1 : Integer N
# Output Format :
# One Line for every board configuration. 
# Every line will have N*N board elements printed row wise and are separated by space
# Note : Don't print anything if there isn't any valid configuration.
# Constraints :
# 1<=N<=10
# Sample Input 1:
# 4
# Sample Output 1 :
# 0 1 0 0 0 0 0 1 1 0 0 0 0 0 1 0 
# 0 0 1 0 1 0 0 0 0 0 0 1 0 1 0 0 

def isSafe(row, col, board, n):
    i = row-1
    while i >= 0:
        if board[i][col] == 1:
            return False
        i -= 1
    
    i = row-1
    j = col-1
    while i>=0 and j>=0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i = row-1
    j = col+1
    while i>=0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True


def printPathsHelper(row, n, board):

    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
        print()
        return
    
    for col in range(n):
        if isSafe(row, col, board, n):
            board[row][col] = 1
            printPathsHelper(row+1, n, board)
            board[row][col] = 0
            

def printPaths(n):
    board = [[0 for j in range(n)] for i in range(n)]
    printPathsHelper(0, n, board)

n = int(input())
printPaths(n)
