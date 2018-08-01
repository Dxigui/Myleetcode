# -*- coding: utf-8 =*=

# 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
# 水平翻转图片就是将图片的每一行都进行翻转，即逆序。
# 例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
# 反转图片的意思是图片中的 0 全部被 1 替换，
# 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。


# 第一种解法
# 循环遍历 A 矩阵
# 先进行倒序在进行替换
def flipAndInvertImage(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    B = []
    for i in A:
        i.reverse()
        C = []
        for j in i:
            if j == 1:
                j = 0
                C.append(j)
            else:
                j = 1
                C.append(j)
        B.append(C)
    return B

# 第二种解法
# 利用列表生成式
# 先利用减法运算符进行替换再切片倒序
def flipAndInvertImage2(A):
    return [[1-j for j in i][::-1] for i in A]


# 第三种解法
# len 函数取得 A 长度，然后利用 for 循环取得索引
# 通过切片对其进行替换
# 通过 map 和 lambda 实现替换
def flipAndInvertImage3(A):
    C = []
    for i in range(len(A)):
        C.append(list(map(lambda x: 1-x, A[i][::-1])))
    return C

print(flipAndInvertImage([[1,1,0,1],[1,0,0,1],[0,0,0,0],[1,0,0,1]]))
