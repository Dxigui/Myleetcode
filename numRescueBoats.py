# -*- coding: utf-8 -*-


# 第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。
# 每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
# 返回载到每一个人所需的最小船数。(保证每个人都能被船载)。


# 这题限制了每艘船最多只能同时载两人，且重量之和不能超过限重（limit）
# 所以两个人的最优组合是最大重量和最小重量小于等于 limit
# 按照这个解题思路
# 先对 people 进行升序排序
# 确定初始索引和结束索引
# people[s] + people[e] <= limit 判断最大重量，最小重量之和
# 如果两者之和小于那么能够被船承载，然后改变索引判断下一个最大值和最小值
# 如果两者之和大于 limit，那么最大值被筛选出并单独坐一艘船，
# 修改结束索引

def numRescueBoats(people, limit):
    people.sort()
    length = len(people)
    s, e = 0, length-1
    count = 0
    while s <= e:
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
        else:
            e -= 1
        count += 1
    return count


if __name__ == '__main__':
    n = numRescueBoats([1,2,3,4,5], 4)
    print(n)
