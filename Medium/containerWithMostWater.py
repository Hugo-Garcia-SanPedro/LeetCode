from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Start pointers at the very left and very right of the array
        left = 0
        right = len(height) - 1
        max_area = 0

        # Move pointers inward until they meet
        while left < right:
            # The width is the distance between the two indices
            width = right - left
            
            # The container's height is bottlenecked by the shorter line
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # Keep track of the largest area seen so far
            if current_area > max_area:
                max_area = current_area
                
            # Crucial logic: Always move the pointer pointing to the shorter line. 
            # Moving the taller line inward can't possibly increase our area, 
            # because the height is still limited by that shorter line, and the width just decreased.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

if __name__ == "__main__":
    solution = Solution()

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    result = solution.maxArea(height=height)
    print(f"The full array is: {height}, the output is: {result}.")