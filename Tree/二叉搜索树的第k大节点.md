逆向中序遍历
灵活处理
```py
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        stack = []
        ans = -1
        while stack or root:
            while root:
                stack.append(root)
                root = root.right
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.left
        
        return ans
```
