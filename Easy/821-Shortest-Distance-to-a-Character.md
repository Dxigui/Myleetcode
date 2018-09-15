## 821. Shortest Distance to a Character

 Given a string `S` and a character `C`, return an array of integers representing the shortest distance from the character `C` in the string.

**Example 1:**

```
Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
```

 

**Note:**

1. `S` string length is in `[1, 10000].`
2. `C` is a single character, and guaranteed to be in string `S`.
3. All letters in `S` and `C` are lowercase.

```python
# TODO
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        len_S = len(S)
        right_e = 0
        left_e = 0
        index_e = 0
        distance = []
        for s in range(len_S):
            num = s
            # 当与 e 重合时找下一个 e 的位置
            if num >= left_e:
                # 
                while True:
                    
                    if num > len_S -1:
                        break
                    if S[num] == C:
                        index_e = num
                        right_e = left_e
                        left_e = num
                        break
                    num += 1
            if S[0] != C:
                if right_e == 0:
                    distance.append(abs(s-left_e))
                elif abs(s - left_e) >= abs(s - right_e):
                    distance.append(abs(s - right_e))
                else:
                    distance.append(abs(s - left_e))
            else:
                if abs(s - left_e) >= abs(s - right_e):
                    distance.append(abs(s - right_e))
                else:
                    distance.append(abs(s - left_e))
        return distance
```

