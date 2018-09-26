## 数值的整数次方

给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。



```python
def power(base, exponent):
    if base == 0:
        return 0
    if exponent == 0:
        return 1
    exp = abs(exponent)
    tmp = base
    res = 1
    while exp > 0:
        if exp & 1 == 1:
            res *= tmp
        exp = exp >> 1
        tmp *= tmp
    return res if exponent > 0 else 1/res
```

