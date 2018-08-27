## 500. Keyboard Row

Given a List of words, return the words that can be typed using letters of **alphabet** on only one row's of American keyboard like the image below. 

**Example 1:**

```
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
```

**Note:**

1. You may use one character in the keyboard more than once.
2. You may assume the input string will only contain letters of alphabet.

```python
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        top = 'qwertyuiop'
        middle = 'asdfghjkl'
        boot = 'zxcvbnm'
        new_words = []
        for word in words:
            ps = False
            w = word.lower()
            if w[0] in top:
                for s in w:
                    if s not in top:
                        ps = True
            elif w[0] in middle:
                for s in w:
                    if s not in middle:
                        ps = True
            else:
                for s in w:
                    if s not in boot:
                        ps = True
            if not ps:
                new_words.append(word)
        return new_words

class Solution:
    def findWords(self, words):
        top = 'qwertyuiopQWERTYUIOP'
        middle = 'asdfghjklASDFGHJKL'
        bottom = 'ZXCVBNMzxcvbnm'
        new_words = []
        for word in words:
            i = 0
            if word[0] in top:
                line = top
            elif word[0] in middle:
                line = middle
            else:
                line = bottom
            for s in word:
                if s not in line:
                    break
                elif i == len(word) - 1:
                    new_append(s)
                else:
                    i += 1
        return new_words
```

