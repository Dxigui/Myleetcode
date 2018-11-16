## 栈的压入,弹出序列

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）



思路:

* 引入辅助栈 `stack`
* 判断 `pushV[0]` 和 `popV[0]` 相等则直接删除
* 判断 `stack[-1]` 和 `popV[0]` 相等则删除
* 判断 `pushV` 是否为空,不为空则将 `pushV` 压入辅助栈,然后重新进行第一步.

```python
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False
        stack = []
        while popV:
            if pushV and pushV[0] == popV[0]:
                pushV.pop(0)
                popV.pop(0)
            elif stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            elif pushV:
                stack.append(pushV.pop(0))
            # 上面的条件如果不成立则不成立
            else:
                return False
        return True
```

