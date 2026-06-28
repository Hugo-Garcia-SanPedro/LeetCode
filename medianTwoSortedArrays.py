from typing import List
import math

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
        for i in range((n + m) - 1):
            if finalArray[i] > finalArray[i + 1]:
                alternative = finalArray[i + 1]
                finalArray[i + 1] = finalArray[i]
                finalArray[i] = alternative

        # Next we calculate the median
        if ((n + m) % 2) == 0:
            half1 = math.trunc((n + m) / 2)
            half2 = half1 + 1
            median = (half1 + half2) / 2
        else:
            half = math.trunc((n + m) / 2)
            median = finalArray[half + 1]

        return median

if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 3]
    nums2 = [2]

    median = solution.findMedianSortedArrays(nums1=nums1, nums2=nums2)
    print(f"The median of {nums1} and {nums2} are: {median}.")