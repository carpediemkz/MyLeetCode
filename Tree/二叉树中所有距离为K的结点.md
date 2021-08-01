给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。


灵活广搜


```py
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def markP(dic, root, target):
            q = deque()
            q.append(root)
            while q:
                l = len(q)
                for i in range(l):
                    cur = q.popleft()
                    if cur.left:
                        q.append(cur.left)
                        dic[cur.left] = cur
                        if cur.left == target:
                            break
                    if cur.right:
                        q.append(cur.right)
                        dic[cur.right] = cur
                        if cur.right == target:
                            break
            newdic = {}
            x = target
            while x and x in dic:
                newdic[x] = dic[x]
                x = dic[x]
            dic = newdic
            return

        
        dic = {}
        ans = []
        markP(dic, root, target)
        
        q = deque()
        q.append(target)
        visited = set()
        while k > 0:
            k -= 1
            l = len(q)
            for i in range(l):
                cur = q.popleft()
                visited.add(cur)
                if cur.left and cur.left not in visited:
                    q.append(cur.left)
                if cur.right and cur.right not in visited:
                    q.append(cur.right)
                if cur in dic and dic[cur] not in visited:
                    q.append(dic[cur])
               

        return [x.val for x in q]
```