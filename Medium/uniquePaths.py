class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Fist we make the grid
        grid = [["."] * n for i in range(m)]
        res = []

        # Backtracking
        def backtrack(row):
            if row == m:
                copy = ["".join(rowGrid) for rowGrid in grid]
                res.append(copy)
                return

            for column in range(n):
                if self.isValid(row, column, grid):
                    grid[row][column] = "X"
                    backtrack(row + 1)
                    grid[row][column] = "."

        backtrack(0)
        return len(res)

    def isValid(n: int, m: int, grid):

if __name__ == "__main__":
    solutions = Solution()
    m = 3
    n = 7
    output = solutions.uniquePaths(m=m, n=n)
    print(f"Las posibles soluciones son: {output}.")