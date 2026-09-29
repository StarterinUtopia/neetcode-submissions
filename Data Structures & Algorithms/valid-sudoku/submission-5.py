import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row=board[i]
            seen=set()
            for r in row:
                if r !='.' :
                    if r in seen:
                        return False
                    seen.add(r)
        for i in range(9):
            column=[board[row][i] for row in range(9)]
            seen=set()
            for c in column:
                if c !='.' :
                    if c in seen:
                        return False
                    seen.add(c)
                
        for i in range(9):
            seen=set()
            for m in range(3):
                for n in range(3):
                    row = (i//3)*3+m
                    col = (i%3)*3+n  
                    if board[row][col] !='.' :
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])
        return True