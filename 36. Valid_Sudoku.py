# https://leetcode.com/problems/valid-sudoku/description/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # checking rows
        for i in range(9):
            # Separate set for each row
            row = set()
            for j in range(9):
                # board[0][0], board[0][1], board[0][2]...
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])

        # checking cols
        for j in range(9):
            col = set()
            for i in range(9):
                # board[0][0], board[1][0], board[2][0]...
                if board[i][j] != '.':
                    if board[i][j] in col:
                        return False
                    col.add(board[i][j])
        
        # checking sub-box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = set()
                for m in range(3):
                    for n in range(3):
                        if board[i + m][j + n] != '.':
                            if board[i + m][j + n] in sub_box:
                                return False
                            sub_box.add(board[i + m][j + n])      

        return True  



        
