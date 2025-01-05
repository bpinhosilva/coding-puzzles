from typing import Optional

"""
Description: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
Time Complexity: O(n)
Space Complexity: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def is_tail(self, node: ListNode) -> bool:
        return node and not node.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = head
        r = head

        for i in range(n):
            if self.is_tail(r):
                head = head.next
                return head

            r = r.next

        while not self.is_tail(r):
            r = r.next
            l = l.next

        l.next = l.next.next

        return head


if __name__ == "__main__":
    pass
