## 二叉树深度

输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

思路:

1. 层次遍历

用队列辅佐,将二叉树的每一层节点都入队列,然后依次出队列,并判断出队列的节点是否有子节点,有则将子节点也入队列

```python
# -*- coding: utf-8 -*-

class Solution(object):
    def levelOrder(self, node):
        # 存储所有节点
        all_node = []
        # 二叉树深度
        count = 0
        # 队列
        q = []
        # 将根节点入队列
        q.append(node)
        while len(q) != 0:
            # 存储同层节点
            tmp = []
            # 记录同层节点数
            length = len(q)
            for i in range(length):
                # 将同层节点出队列
                n = q.pop(0)
                if n.left != None:
                    q.append(n.left)
                if n.right != None:
                    q.append(n.right)
                tmp.append(n.val)
            if tmp:
                count += 1
            all_node.append(tmp)
        return count

    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        count = self.levelOrder(pRoot)
        return count
```

2. 递归实现

```python
class Solution(object):
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
        
```

