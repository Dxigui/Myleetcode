# -*- coding: utf-8 -*-

# 给定一个正整数，输出它的补数。补数是对该数的二进制表示取反

# 第一种解法 用时 48ms
# 利用 format 函数将整数转换为二进制并且去掉其导零位（如果保留导零位后面参数为 '#b'）
# 然后遍历二进制字符串并通过减法运算的方式对其取反
# 取反后进行字符串拼接，得到反转后的二进制字符串
# 再通过 int 函数将新的二进制转换为新的十进制
# int 的第一个参数为二进制字符串，第二个参数为进位制如这里的 2
def findComplement(num):
    bin_num = format(num, 'b')
    return int(''.join([str(1-int(x)) for x in bin_num]), 2)

print(findComplement(100))


# 第二种解法 32ms
def findComplement2(num):
    mask = 0
    while mask < num:
        mask <<= 1
        mask |= 1
    return num ^ mask

print(findComplement2(5))


# 第三种解法 36ms
def findComplement3(num):
    s = bin(num)[2:]
    s = s.replace('0', '2').replace('1','0').replace('2', '1')
    num = 0
    for i in range(len(s)-1, -1, -1):
        num += int(s[i])*2**(len(s) - i -1)
    return num

print(findComplement3(5))

# 第四种解法 56ms
def findComplement4(num):
    for idx in range(32):
        if num < 2**idx:
            return 2**idx-num-1
print(findComplement4(100))


# 第五种解法
def findComplement5(num):
    a,b = bin(num)[2:], ['1', '0']
    res = ''.join([b[int(i)] for i in a])
    return int(res, 2)

# 第六种解法
def findComplement6(num):
    return 2 ** (len(bin(num)) -2) - num -1
