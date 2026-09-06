from typing import List

class Solution:
    def totalNQueens(self, n: int) -> int:
        # Fist the variable we need
        solutions = 0
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(row):
            # Next the base problem
            if row == n:
                copy = ["".join(rowBoard) for rowBoard in board]
                res.append(copy)
                solutions = solutions + 1
                return

            for column in range(n):
                if self.isSafe(row, column, board):
                    # Fisrt we move the queen
                    board[row][column] = "Q"
                    # Second we do the backtracking
                    backtrack(row + 1)
                    board[row][column] = "."

        backtrack(0)
        return solutions