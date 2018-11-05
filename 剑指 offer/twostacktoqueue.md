## 用两个栈实现队列  
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型.  

思路:
* 栈先进后出(FILO),队列先进先出(FIFO)
* 判断栈 B 中是否为空,如果不为空则直接出栈,为空则判断栈 A 中是否为空,不为空则栈 A 出栈到栈 B,然后 B 再出栈,让两栈实现一个队列  

```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        # 创建栈 A,B
        self.stackA = []
        self.stackB = []
    def push(self, node):
        # 将值压入栈 A
        self.stackA.append(node)
    def pop(self):
        # 判断栈 B 是否为空
        if self.stackB:
            return self.stackB.pop()
        # 判断栈 A 是否为空
        if self.stackA:
            while self.stackA:
                # 栈 A 入栈 B
                self.stackB.append(self.stackA.pop())
        else:
            return None
        return self.stackB.pop()
```
