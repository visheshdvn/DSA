# Given a 9*9 sudoku board, in which some entries are filled and others are 0 (0 indicates that the cell is empty), you need to find out whether the Sudoku puzzle can be solved or not i.e. return true or false.
# Input Format :
# 9 Lines where ith line contains ith row elements separated by space
# Output Format :
#  true or false
# Sample Input :
# 9 0 0 0 2 0 7 5 0 
# 6 0 0 0 5 0 0 4 0 
# 0 2 0 4 0 0 0 1 0 
# 2 0 8 0 0 0 0 0 0 
# 0 7 0 5 0 9 0 6 0 
# 0 0 0 0 0 0 4 0 1 
# 0 1 0 0 0 5 0 8 0 
# 0 9 0 0 7 0 0 0 4 
# 0 8 2 0 4 0 0 0 6
# Sample Output :
# true

def notInBox(arr, startRow, startCol):
    st = set()

    for row in range(0, 3):
        for col in range(0, 3):
            curr = arr[row + startRow][col + startCol]

            if curr in st:
                return False

            if curr != 0:
                st.add(curr)

    return True

def notInCol(arr, col):
    st = set()

    for i in range(0, 9):

        if arr[i][col] in st:
            return False

        if arr[i][col] != 0:
            st.add(arr[i][col])

    return True


def notInRow(arr, row):
    st = set()

    for i in range(0, 9):

        if arr[row][i] in st:
            return False

        if arr[row][i] != 0:
            st.add(arr[row][i])

    return True

def isValid(arr, row, col):
    return (notInRow(arr, row) and notInCol(arr, col) and
            notInBox(arr, row - row % 3, col - col % 3))


def solveSudoku(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if not isValid(board, i, j):
                return False
    return True

board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solveSudoku(board)
if ans:
    print('true')
else:
    print('false')