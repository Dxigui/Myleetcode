## 884. Uncommon Words from Two Sentences

We are given two sentences `A` and `B`.  (A *sentence* is a string of space separated words.  Each *word* consists only of lowercase letters.)

A word is *uncommon* if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 


**Example 1:**

```
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
```

**Example 2:**

```
Input: A = "apple apple", B = "banana"
Output: ["banana"]
```

 

**Note:**

1. `0 <= A.length <= 200`
2. `0 <= B.length <= 200`
3. `A` and `B` both contain only spaces and lowercase letters.



解答:

这题时在两个由空格隔开的两个字符串中找出不重复的词.

主要有两点:

* 单个字符串内不重复
* 两个字符串内不重复

所以这题可以先通过字符串 `split()`  方法实现去空格,并以列表形式返回,然后可以分开比较两个列表是否存在重复,不过更好的是先合并这两个列表在通过 `count()`  方法判断是否重复

```python
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        # new_A = A.split()
        # new_B = B.split()
        L = []
        
#         for i in new_A:
        
#             if i not in new_B and new_A.count(i) == 1:
#                 print(i)
#                 L.append(i)
#         for j in new_B:
#             if j not in new_A and new_B.count(j) == 1:
#                 print(j)
#                 L.append(j)
        new_AB = (A + ' ' + B).split()
        for word in new_AB:
            if new_AB.count(word) == 1:
                L.append(word)
        return L
```

