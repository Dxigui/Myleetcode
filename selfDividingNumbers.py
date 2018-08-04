# -*- coding: utf-8 -*-

# 自除数 是指可以被它包含的每一位数除尽的数。
#例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
#还有，自除数不允许包含 0 。
#给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

def selfDividingNumbers(left,right):
    num_iter = (str(n) for n in range(left,right+1) if '0' not in str(n))
    print(num_iter)
    dividingnumber = []
    for num in num_iter:
        print(num)
        count = 0
        for i in range(len(num)):
            if int(num)%(int(num[i])) == 0:
                count += 1
                continue
            else:
                break
        if count == len(num):
            dividingnumber.append(int(num))
    return dividingnumber
    

print(selfDividingNumbers(1,22))
