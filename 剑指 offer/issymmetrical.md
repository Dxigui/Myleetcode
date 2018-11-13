## 对称二叉树

请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。



```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.compare(pRoot.left, pRoot.right)
    
    def compare(self, pleft, pright):
        if not pleft and not pright:
            return True
        if not pleft or not pright:
            return False
        if pleft.val == pright.val:
            if self.compare(pleft.left, pright.right) and self.compare(pleft.right, pright.left):
                return True
        return False
```

