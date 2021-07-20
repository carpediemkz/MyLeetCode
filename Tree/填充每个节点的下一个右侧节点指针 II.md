层序遍历也是一种解
这是利用已有的next信息进行连接的解
```py
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        if root.left:
            if root.right:
                root.left.next = root.right
            elif root.next:
                n = root.next
                while n and (root.left.next is None):
                    if n.left:
                        root.left.next = n.left
                    elif n.right:
                        root.left.next = n.right
                    n = n.next
        if root.right:
            if root.next:
                n = root.next
                while n and (root.right.next is None):
                    if n.left:
                        root.right.next = n.left
                    elif n.right:
                        root.right.next = n.right
                    n = n.next

        self.connect(root.right)
        self.connect(root.left)
        return root
```