## 二叉树的下一个节点

给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

思路

> 因为中序遍历遵循LVR的顺序，其中L为左子树，V为节点值，R为右子树。
> 根据所给节点与其他节点的关系，分类讨论：
> 1>所给节点如果有右孩子，则直接返回右孩子；
> 2>否则，如果所给节点没有父节点，当前节点为没有右子树的根节点，返回NULL；
> 3>否则，如果所给节点为父节点的左孩子，直接返回父节点；
> 4>否则，沿父节点向上，直到找到一个节点x，满足：
> ​    pNode位于x节点的左子树 && pNode位于x左孩子的右子树
> ​    返回x节点。



```python
# -*- coding:utf-8 -*-
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution(object):
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        while pNode.next:
            if pNode.next.left == pNode:
                return pNode.next
            pNode = pNode.next
        return
```

