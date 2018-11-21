## 二叉树中和为某一值的路径

输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

思路:

* 利用递归遍历二叉树
* 记录当前的路径(入栈)以及目标值和节点的差值
* 只有在满足节点为叶节点并且目标值为 0 时,那么将这一路径添加到返回列表中
* 删除叶节点(出栈),继续递归判断右节点

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.path = []
        self.result = []
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return self.result
        self.path.append(root)
        expectNumber -= root.val
        if expectNumber == 0 and root.left is None and root.right is None:
            self.result.append([p.val for p in self.path])
        self.FindPath(root.left, expectNumber)
        self.FindPath(root.right, expectNumber)
        self.path.pop()
        return self.result.sort(reverse=True)

```

