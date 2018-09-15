### 问题

在不使用除法/乘法以及 `for while if ` 等判断和循环语句的前提下,求 `1 + 2 + 3 + ... + n` 的和.

### 答案

通过 `and` 短路原则实现递归结束条件.

```python
def sum_solution(n):
    res = n
    print('这是递归时的res, n:',res,n)
    # and 短路原则
    # 当 and 的两边有一边为 False 时,返回 False 这一边
        # 0 and 1 ==> 0    1 and 0 ==> 0
    # 当 and 的两边都为 True 时,返回右边
        # 1 and 2 ==> 2
    # 当 and 的两边都为 False 时,返回 左边

    # 这里 n 没有变为 0 时,一直执行右边的递归 sum_solution
    # 当 n=0 时,返回左边 res

    # 这里的 temp 的值是 res and sum_solution(n - 1) 的返回值
    temp = (res and sum_solution(n - 1))
    print('递归结束后的temp, res:',temp,res)
    res += temp
    print('这是递归结束后的res:',res)
    print('-'*20)
    return res

if __name__ == '__main__':
    print(sum_solution(5))
```

### and 和 or

1. `and` 短路原则

   * 当 `and` 两侧都为 `True` 时,返回右边的 `True`

     ```python
     >>> True and 'right'
     'right'   # 返回右边的 'right'
     >>> 'left' and True
     True      # 返回右边的 True
     ```

   * 当 `and` 有一侧为 `True` 一侧为 `False` 时,返回 `False`

     ```python
     >>> True and False
     False    # 返回右边的 False
     >>> False and True
     False    # 返回左边的 False
     ```

   * 当 `and` 两侧都为 `False` 时,返回左边的 `False`

     ```python
     >>> False and 0
     False    # 返回左边的 False
     >>> 0 and False
     0        # 返回左边的 0
     ```

2. `or`

   * 当 `or` 两侧都为 `True` 时,返回左侧的 `True`

     ```python
     >>> True or 'right'
     True    # 返回左边的 True
     >>> 'left' or True
     'left'  # 返回左边的 'left'
     ```

   * 当 `or` 一侧为 `True` ,一侧为 `False` 时,返回 `True`

     ```python
     >>> True or False
     True    # 返回左边的 True
     >>> False or True
     True    # 返回右边的 True
     ```

   * 当 or 两侧都为 `False` 时, 返回右边的 `False`

     ```python
     >>> False or 0
     0       # 返回右边的 0
     >>> 0 or False 
     False   # 返回右边的 False
     ```

`and` 和 `or`  在两侧条件相同的情况下,其返回值正好相反.