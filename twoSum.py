from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

if __name__ == "__main__":
    solution = Solution()

    array_numbers = [2, 7, 11, 15]
    objective = 9

    result = solution.twoSum(nums=array_numbers, target=objective)
    print(f"The indexes that sum {objective} are: {result}")