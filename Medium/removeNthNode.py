from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast hits the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the target node
        slow.next = slow.next.next

        return dummy.next


def build_linked_list(values: list) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def linked_list_to_list(node: Optional[ListNode]) -> list:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    solution = Solution()

    values = [1, 2, 3, 4, 5]
    n = 2

    head = build_linked_list(values) 
    result_node = solution.removeNthFromEnd(head=head, n=n)
    result = linked_list_to_list(result_node)

    print(f"The result is {result}")