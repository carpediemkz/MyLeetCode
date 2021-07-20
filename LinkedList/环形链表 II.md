```py
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                pt = head
                while pt!=slow:
                    pt = pt.next
                    slow = slow.next
                return pt
        return None
```