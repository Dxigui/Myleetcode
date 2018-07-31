# -*- coding: utf-8 -*-

# 短字符串在长字符串中出现的次数
# 第一种解法（）
# 利用循环遍历长字符串，再判断遍历出的字符是否在短字符中
# 如果在则计数加 1，最后统计处总出现次数
class Solution(object):
    def numJewelsInStones(self, J, S):
        count = 0
        ListJ = list(J)
        for i in S:
            if i in ListJ:
                count += 1
        return count

solution = Solution()
print(solution.numJewelsInStones('adfKJNFi', 'aoifejfkmaklnmvklksdjfKLJKJDSLKJLjkl'))


# 第二种解法
# 
class Solution2(object):
    def numJewelsInStones2(self, J, S):
        for i in (s in J for s in S):
            print(i)
        return sum(s in J for s in S)

solution2 = Solution2()
print(solution2.numJewelsInStones2('adfKJNFi', 'aoiejfkmaklnmvklksdjfKLJKJDSLKJLjkl'))


# 第三种解法
# 利用 Python Set 里 x in s 最优时间复杂度为 O（1）
# 
class Solution3(object):
    def numJewelsInStones3(self, J, S):
        setJ = set(J)
        return sum(s in setJ for s in S)

# 第四种解法
# 利用列表生成式，遍历长字符串，判断遍历出的字符是否在短字符中
# 将返回的字符生成一个列表
class Solution4(object):
    def numJewelsInStones4(self, J, S):
        print(type([stone for stone in S if stone in J]))
        return len([stone for stone in S if stone in J])
solution4 = Solution4()
print(solution4.numJewelsInStones4('adfKJNFi', 'aoiejfkmaklnmvklksdjfKLJKJDSLKJLjkl'))

