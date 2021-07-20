两层循环进行处理
```py
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        pt = dummy
        while pt.next and pt.next.next:
            if pt.next.val == pt.next.next.val:
                temp = pt.next
                while temp and temp.val == pt.next.val:
                    temp = temp.next
                pt.next = temp
            else:
                pt = pt.next
        return dummy.next
```