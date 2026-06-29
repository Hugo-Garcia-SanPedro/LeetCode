from typing import List
import math
import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        finalArray = []

        # First we have to join the 2 arrays
        for i in range(n):
            finalArray.append(nums1[i])
        for j in range(m):
            finalArray.append(nums2[j])

        # Next I order the array
        ordenated = sorted(finalArray)
        order = len(ordenated)

        # Calculate the median
        if (order) % 2 == 0:
            mid = (order) // 2
            number1 = ordenated[mid - 1 ]
            number2 = ordenated[mid]
            median = (number1 + number2) / 2
        else:
            mid = (n + m) // 2
            median = ordenated[mid]

        return median

if __name__ == "__main__":
    solution = Solution()

    nums1 = [2, 5, 3]
    nums2 = [9, 1, 5, 2]

    median = solution.findMedianSortedArrays(nums1=nums1, nums2=nums2)
    print(f"The median of {nums1} and {nums2} are: {median}.")