## 斐波那契数列

大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。

n<=39

思路:

1. 可以使用递归

递归的时间复杂度高

```python
# -*- coding:utf-8 -*-
class Solution(object):
    def __init__(self):
        pass

    def fibonacci(self, count):
        if count == 0:
            return 0
        if count == 1:
            return 1
        result = self.fibonacci(count-1) + self.fibonacci(count-2)
        return result

    def Fibonacci(self, n):
        # write code here
        count = 0
        while count != n:
            count += 1
        return self.fibonacci(count)

```



2. 使用动态规划

速度快而且不用担心栈溢出

```python
class Solution(self):
    def Fibonacci(self, n):
        f = 0
        s = 1
        while n > 0:
            g += f
            f = g - f
            n -= 1
        return f
```

