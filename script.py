import os
titles = [

"平衡二叉树",

"二叉树的深度",

"对称的二叉树",

"二叉树的镜像",

"二叉树的最近公共祖先",

"相同的树",

"从上到下打印二叉树",

"二叉搜索树的最近公共祖先",

"合并二叉树",

"平衡二叉树",

"实现 Trie (前缀树)",

"对称二叉树",

"翻转二叉树",

"从上到下打印二叉树 III",

"从上到下打印二叉树 II",

"二叉搜索树的第k大节点",

"二叉搜索树的后序遍历序列",

"验证二叉搜索树",

"恢复二叉搜索树",

"修剪二叉搜索树",

"二叉树的直径",

"二叉树中和为某一值的路径",

"不同的二叉搜索树",

"二叉树的右视图",

"二叉树的所有路径",

"完全二叉树的节点个数",

"二叉搜索树中的搜索",

"二叉树的最大深度",

"找树左下角的值",

"二叉树展开为链表",

"二叉树的最近公共祖先",

"二叉树的最小深度",

"不同的二叉搜索树 II",

"有序链表转换二叉搜索树",

"二叉搜索树中的插入操作",

"删除二叉搜索树中的节点",

"二叉搜索树的最近公共祖先",

"二叉树的层序遍历",

"二叉搜索树节点最小距离",

"二叉树的后序遍历",

"二叉树的中序遍历",

"二叉树的前序遍历",

"将有序数组转换为二叉搜索树",

"二叉搜索树的最小绝对差",

"二叉树的层序遍历 II",

"二叉树中的最大路径和",

"二叉树的锯齿形层序遍历",

"二叉搜索树中第K小的元素",

"水果成篮",

"左叶子之和"
]

for t in titles:
    fp = open("./Tree/{}.md".format(t), "w")
    fp.writelines(
"""
```py

```
""")
    fp.close()
