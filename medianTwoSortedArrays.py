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
        for i in range((n + m) - 1):
            if finalArray[i] > finalArray[i + 1]:
                alternative = finalArray[i + 1]
                finalArray[i + 1] = finalArray[i]
                finalArray[i] = alternative

        # Calculate the median
        if (n + m) % 2 == 0:
            mid = (n + m) // 2
            number1 = finalArray[mid - 1]
            number2 = finalArray[mid]
            median = (number1 + number2) / 2
        else:
            mid = (n + m) // 2
            median = finalArray[mid]

        return median

if __name__ == "__main__":
    solution = Solution()

    nums1 = [0, 0]
    nums2 = [0, 0]

    median = solution.findMedianSortedArrays(nums1=nums1, nums2=nums2)
    print(f"The median of {nums1} and {nums2} are: {median}.")