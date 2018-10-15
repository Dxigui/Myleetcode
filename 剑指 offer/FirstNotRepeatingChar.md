## 第一个只出现一次的字符

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

思路:

1. 正常的 python 实现
   * 直接用循环和字符串 `count()` 方法计算字符出现次数

```python
class Solution(object):
    def FirstNotRepeatingChar(self, s):
        if s == '':
            return -1
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
```

2. 对每个字符进行统计,最后结果为 1 的为只出现一次的字符,每个字符的位置为字符自身的 ASCII 码

```python
class Solution(object):
    def FirstNotRepeatingChar(self, s):
        # write code here
        s_num = [0]*256
        for i in s:
            s_num[ord(i)] += 1
        index = 9999
        if 1 not in s_num:
            return -1
        for i,value in enumerate(s_num):
            if value == 1:
                to_s = chr(i)
                i_index = s.find(to_s)
                if index > i_index:
                    index = i_index
        return index


if __name__ == "__main__":
    s = 'sfhFDGHthJTrSFASDFsafsdfsFSfsfADFsfSFSFsFSFSdfsFSFs'
    test = Solution()
    t = test.FirstNotRepeatingChar(s)
    spend = time.time()-start
    print(t)
```

