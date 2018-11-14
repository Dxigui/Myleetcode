## 把二叉树打印成多行  
从上到下按层打印二叉树,同一层节点从左至右输出.每一层输出一行.  

```python
# 层次遍历  
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot:
            return []
        treeToList = []
        qu = []
        qu.append(pRoot)
        while qu is not []:
            mid = []
            lenght = len(qu)
            for _ in range(lenght):
                node = qu.pop(0)
                if node.left is not None:
                    qu.append(node.left)
                if node.right is not None:
                    qu.append(node.right)
                mid.append(node.val)
            treeToList.append(mid)
        return treeToList
```
