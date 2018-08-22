##  806.Number of Lines To Write String

We are to write the letters of a given string `S`, from left to right into lines. Each line has maximum width 100 units, and if writing a letter would cause the width of the line to exceed 100 units, it is written on the next line. We are given an array `widths`, an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.

Now answer two questions: how many lines have at least one character from `S`, and what is the width used by the last such line? Return your answer as an integer list of length 2.

 

```
Example :
Input: 
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
Output: [3, 60]
Explanation: 
All letters have the same length of 10. To write all 26 letters,
we need two full lines and one line with 60 units.
```

```
Example :
Input: 
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"
Output: [2, 4]
Explanation: 
All letters except 'a' have the same length of 10, and 
"bbbcccdddaa" will cover 9 * 10 + 2 * 4 = 98 units.
For the last 'a', it is written on the second line because
there is only 2 units left in the first line.
So the answer is 2 lines, plus 4 units in the second line.
```

 

**Note:**

- The length of `S` will be in the range [1, 1000].
- `S` will only contain lowercase letters.
- `widths` is an array of length `26`.
- `widths[i]` will be in the range of `[2, 10]`.

思路

* 获取 S 每个字符的索引,根据索引得所对应的长度

```python
class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        strToDict = {k:v for v,k in enumerate(list("abcdefghijklmnopqrstuvwxyz"))}
        # allStr = "abcdefghijklmnopqrstuvwxyz"
        row = 1
        colume = 0
        for s in S:
            s_length = widths[strToDict[s]]
            # s_length = widths[allStr.index(s)]
            num = s_length + colume
            if num <= 100:
                colume += s_length
            else:
                colume = s_length
                row += 1
        return [row, colume]
        
class Solution:
    def numberOfLines(self, widths, S):
        row = 1
        colume = 0
        for s in S:
            # ord() 函数返回一个字符得 ASCII 码
            s_length = widths[ord(s) - ord('a')]
            colume += s_length
            if colume > 100:
                row += 1
                colume = s_length
        return [row, colume]
```

