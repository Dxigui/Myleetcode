## 矩形覆盖

我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

思路:

归纳法

* `2*n` 的矩形是在 `2*(n-1)` 的基础上扩展而来, 那么`f(n) = f(n-1) + ?` 
* 对 `n = 1,2,3,4,...` 进行归纳总结可知 `f(n) = f(n-1) + f(n-2)`

* 发现是一个经典的斐波那契规律

1. 递归版

复杂度较大,在用 `Python` 测试时时间较长

```python
class Solution(object):
    def rectCover(number):
    if number < 1: return 0
    if number == 1: return 1
    if number == 2: return 2
    return rectCover(number-1)+rectCover(number-2)
```

2. 迭代斐波那契数列

比递归速度更快

```python
class Solution(object):
    def rectCover(number):
    if number < 1: return 0
    g, f = 1, 2
    while number-1:
        f += g
        g = f - g
        number = number - 1
    return g
```

