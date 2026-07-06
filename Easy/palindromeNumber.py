class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If the number is negative, isn,t palindrome
        if x < 0:
            return False
        num_string = str(x)
        return num_string == num_string[::-1]   

if __name__ == "__main__":
    solution = Solution()

    input = 101

    result = solution.isPalindrome(input)
    print(f"The number {input} is {result}.")