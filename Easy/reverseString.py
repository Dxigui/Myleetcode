# -*- coding: utf-8 -*-

# 344
# Write a function that takes a string as input and returns the string reversed.
# Example:
# Given s = "hello", return "olleh".

# 这题对于 Python 非常简单，直接切片
def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    return s[::-1]
    #ew_s = ''
    #or j in [s[i] for i in range(len(s)-1, -1, -1)]:
    #   new_s += j
    #eturn new_s


# 也可以通过 Python 的 reversed() 内置函数取倒
# 在用 ''.join() 实现字符串拼接
def reverseString2(s):
    return ''.join(reversed(s))

# 递归实现 出自 leetcode --> viakondratiuk
def reverseString3(s):
    l = len(s)
    if l < 2:
        return s
    return reverseString(s[l//2:]) + reverseString(s[:l//2])

# 出自 leetcode --> viakondratiuk
def reverseString4(s):
    r = list(s)
    i, j = 0, len(r) - 1
    while i < j:
        r[i], r[j] = r[j], r[i]
        i += 1
        j -= 1
    return ''.join(r)

if __name__ == '__main__':
    s = 'helloworld'
    r_s1 = reverseString(s)
    r_s2 = reverseString2(s)
    r_s3 = reverseString3(s)
    r_s4 = reverseString4(s)
    print(r_s1, r_s2, r_s3, r_s4)
