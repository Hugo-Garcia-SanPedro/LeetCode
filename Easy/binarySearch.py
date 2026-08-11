from typing import List

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

if __name__ == "__main__":
    solution = Solution()

    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    position = solution.search(nums=nums, target=target)
    print(f"The target {target} in the array {nums} is in the position: {position}.")