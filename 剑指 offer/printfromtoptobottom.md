## 从上往下打印二叉树

从上往下打印出二叉树的每个节点，同层节点从左至右打印。

层次遍历

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        result = []
        qu = []
        qu.append(root)
        while qu:
            lenght = len(qu)
            for _ in range(lenght):
                node = qu.pop(0)
                if node.left is not None:
                    qu.append(node.left)
                if node.right is not None:
                    qu.append(node.right)
                result.append(node.val)
        return result
```

