## 平衡二叉树

输入一颗二叉树,判断该二叉树是否是平衡二叉树.

1. 平衡二叉树
   * 平衡二叉树要么是空树
   * 要么保证左右子树的高度只差不大于 1
   * 子树也必须是一个平衡二叉树
2. 当插入元素到平衡二叉树中时,要判断是否破坏平衡

```python
# -*- coding: utf-8 -*-
# 根据平衡二叉树的性质判断是否为平衡二叉树
# 
class Solution:
    result = True
    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.helper(pRoot)
        return self.result
    def helper(self, pRoot):
        if not pRoot:
            return 0
        if not self.result:
            return 1
        left = 1 + self.helper(pRoot.left)
        right = 1 + self.helper(pRoot.right)
        if abs(left - right) > 1:
            self.result = False
        return max(left, right)
```

