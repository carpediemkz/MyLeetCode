简洁好理解的版本
```py
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        while True:
            step = 0
            while fast and fast.next and step < k:
                fast = fast.next
                step += 1
            if step < k:
                return dummy.next
            pt = slow.next
            step = 0
            while step < k-1:
                step += 1
                
                temp = pt.next
                pt.next = temp.next
                temp.next = slow.next ######
                slow.next = temp
            slow = pt
            fast = pt
```    
        