from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        return dummy

if __name__ == "__main__":
    solution = Solution()

    head = [1, 2, 3, 4, 5]
    n = 2

    array = solution.removeNthFromEnd(head=head, n=n)

    print(f"The result is {array}")