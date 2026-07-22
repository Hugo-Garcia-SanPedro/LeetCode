from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        position = 0
        return position

if __name__ == "__main__":
    solution = Solution()

    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    position = solution.search(nums=nums, target=target)
    print(f"The target {target} in the array {nums} is in the position: {position}.")