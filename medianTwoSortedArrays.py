from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        finalArray = []

        # First we have to join in order the 2 arrays
        for i in range(n):
            for j in range(m):
                if nums1[i] < nums2[j]:
                    finalArray.append(nums1[i])
                else:
                    finalArray.append(nums2[j])

        return finalArray

if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 3]
    nums2 = [2]

    median = solution.findMedianSortedArrays(nums1=nums1, nums2=nums2)
    print(f"The median of {nums1} and {nums2} are: {median}.")