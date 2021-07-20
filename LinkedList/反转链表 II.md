```py
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if right <= left or not head:
            return head
        dummy = ListNode(0, head)
        pt = dummy
        last = dummy
        for i in range(left):
            last = pt
            pt = pt.next
        for i in range(right - left):
            temp = pt.next
            pt.next = pt.next.next
            temp.next = last.next
            last.next = temp
        return dummy.next
```