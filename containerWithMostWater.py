from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        index1 = 0
        index2 = 0
        result = 0

        # Iterate over the array
        for i in range(n):
            base = index2 - index1
            quota = height[i]
            area = base * quota

            if area > result:
                result = area

        return result

if __name__ == "__main__":
    solution = Solution()

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    result = solution.maxArea(height=height)
    print(f"The full array is: {height}, the output is: {result}.")