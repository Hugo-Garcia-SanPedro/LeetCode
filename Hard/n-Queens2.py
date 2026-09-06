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

    def isSafe(self, r: int, c: int, board):
        # First we check the rows
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row = row - 1

        # Second we check the columns
        row = r - 1
        column = c - 1
        while row >= 0 and column >= 0:
            if board[row][column] == "Q":
                return False
            row = row - 1
            column = column - 1

        # Third we check the diagonals
        row = r - 1
        column = c + 1
        while row >= 0 and column < len(board):
            if board[row][column] == "Q":
                return False
            row = row - 1
            column = column + 1

        return True

if __name__ == "__main__":
    solutions = Solution()
    n = 4
    numberSolutions = solutions.totalNQueens(n=n)
    print(f"The total number of solutions is {numberSolutions}.")