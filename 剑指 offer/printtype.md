## 按之字型顺序打印二叉树

请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

思路:

* 层次索引依次遍历整个二叉树,
* 标记当前层数,为奇数层则从左至右,为偶数层则从右往左



```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def __init__(self):
        # 标记当前层数,根节点为第一层
        self.count = 1
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        result = []
        # 将每层节点入队列
        qu = []
        qu.append(pRoot)
        while qu:
            tmp = []
            length = len(qu)
            for _ in range(length):
                node = qu.pop(0)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
                tmp.append(node.val)
            if self.count % 2 == 1:
                result.append(tmp)
            else:
                result.append(tmp[::-1])
            self.count += 1
        return result
```

