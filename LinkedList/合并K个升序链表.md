```py
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = ListNode(1)
            pt = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    pt.next = l1
                    l1 = l1.next
                else:
                    pt.next = l2
                    l2 = l2.next
                pt = pt.next
            if l1:
                pt.next = l1
            if l2:
                pt.next = l2
            return dummy.next
        
        while len(lists) > 1:
            n = int(len(lists) / 2)
            new_list = []
            for i in range(n):
                a = lists[2*i]
                b = lists[2*i + 1]
                new_list.append(mergeTwoLists(a, b))
            if len(lists) == 2 * n + 1:
                new_list.append(lists[2*n])
            lists = new_list
        if lists:
            return lists[0]
        return None
```