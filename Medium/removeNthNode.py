from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head.delete(n)

        return head

if __name__ == "__main__":
    solution = Solution()

    head = [1, 2, 3, 4, 5]
    n = 2

    array = solution.removeNthFromEnd(head=head, n=n)

    print(f"The result is {array}")