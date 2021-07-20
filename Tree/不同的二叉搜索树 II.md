官解，其实是个暴力解
```py
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(left, right):
            if left > right:
                return [None]
            ans = []
            for i in range(left, right+1):
                leftset = dfs(left, i-1)
                rightset = dfs(i+1, right)
                for l in leftset:
                    for r in rightset:
                        tree = TreeNode(i, l, r)
                        ans.append(tree)
            return ans
        return dfs(1, n)
```
