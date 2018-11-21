## 把字符串转换成整数

将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。

## 输入描述:
> 输入一个字符串,包括数字字母符号,可以为空
## 输出描述:
> 如果是合法的数值表达则返回该数字，否则返回0
示例1
## 输入
```
+2147483647
    1a33
```
## 输出
```
2147483647
    0
```



思路:

* 创建一个字符串到数字的字典映射
* 通过 `isinstance` 判断是否为整数,通过异常来判断字符串中是否存在非整数字符串.
* 通过 `reduce` 函数将整数字符串转换为整数

```python
# -*- coding:utf-8 -*-
class Solution(object):
    def toInt(self, x, y):
        return x*10 + y
    def StrToInt(self, s):
        # write code here
        if s == '0' or len(s) == 0:
            return 0
        s_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        tmp = {k:v for k, v in zip(s_num, range(10))}
        flag = '+'
        if s[0] == '+' or s[0] == '-':
            flag = s[0]
            s = s[1:]
        from functools import reduce
        if s == '0' or len(s) == 0:
            return 0
        try:
            result = all([isinstance(tmp[i], int) for i in s])
        except KeyError as e:
            return 0
        if result:
            num = reduce(self.toInt, [tmp[i] for i in s])
            if flag == '+':
                return num
            else:
                return -num
        else:
            return 0
```

