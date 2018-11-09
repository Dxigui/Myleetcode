## 二叉树镜像

操作给定的二叉树，将其变换为源二叉树的镜像。

**输入描述**:

```
二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
```

思路:

* 层次遍历: 利用栈先进后出特征翻转每一层的节点

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return
        # 创建栈
        stack = []
        # 将根节点入栈
        stack.append(root)
        while stack:
            tmp = []
            lenght = len(stack)
            for _ in range(lenght):
                # 将顶部节点弹出栈
                node = stack.pop()
                # 交换当前节点的子节点位置
                if (node.left is not None) or (node.right is not None):
                    mid = node.left
                    node.left = node.right
                    node.right = mid
                if node.left is not None:
                    tmp.append(node.left)
                if node.right is not None:
                    tmp.append(node.right)
            # 将子节点从左至右入栈
            stack.extend(tmp)
        return root
```

* 递归

```python
class Solution(object):
    def Mirror(self, root):
        if not root:
            return root
        node = root.left
        root.left = root.right
        root.right = node
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
```

