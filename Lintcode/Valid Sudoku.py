class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # check rows
        for i in range(9):
            memo = {}
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in memo:
                    return False
                else:
                    memo[board[i][j]] = True

        # check columns
        for j in range(9):
            memo = {}
            for i in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in memo:
                    return False
                else:
                    memo[board[i][j]] = True

        # check 3*3
        for m in range (0, 9, 3):
            for n in range (0, 9 ,3):
                memo = {}
                for i in range(m, m+3):
                    for j in range(n, n+3):
                        if board[i][j] == '.':
                            continue
                        elif board[i][j] in memo:
                            return False
                        else:
                            memo[board[i][j]] = True
        return True
