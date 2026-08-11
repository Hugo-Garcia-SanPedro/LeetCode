from typing import Optional 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return 0

if __name__ == "__main__":
    solution = Solution()

    list1 = Optional[ListNode]
    list2 = Optional[ListNode]
    finalList = solution.mergeTwoLists(list1=list1, list2=list2)

    print(f"First array {list1}, second array {list2}, merge list {finalList}.")