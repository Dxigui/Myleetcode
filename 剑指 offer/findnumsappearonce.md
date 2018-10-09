## 数组中只出现一次的数字  

一个整型数组里除了两个数字之外，其他数字都出现了偶数次，请写程序找出这两个只出现一次的数字。  

```python
def isBit(num, index):
    num = num >> index
    return num & 1

def FindNumsAppearOnce(array):
    if not array:
        return []
    sums = 0
    index = 0
    for i in array:
        sums = sums ^ i
    while (sums & 1) == 0:
        sums >> 1
        index += 1
    a = 0
    b = 0
    for i in array:
        if self.isBit(i, index):
            a = a ^ i
        else:
            b = b ^ i
    return [a, b]
```
