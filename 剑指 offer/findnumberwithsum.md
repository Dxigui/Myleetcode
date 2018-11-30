## 和为S的两个数字

输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的.

思路:

* 因为数组为递增的,所以可以建立头部和尾部双指针 `start` 和 `end`.
* 然后对分别判断`大于/等于/小于` 三种情况
* 当两个数的和大于 `S` 时,即当前数组的最大值和最小值的和大于 `S`,所以可以排除最大值,即 `end - 1`
* 当两个数的和小于 `S` 时,即当前数组的最大值和最小值的和小于 `S` ,所以可以排除最小值,即 `start + 1`
* 当两个数的和等于 `S` 时,即 `start + 1 and end - 1`



```python
# -*- coding:utf-8 -*-
class Solution(object):
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if array == []:
            return []
        start = 0
        end = len(array)-1
        result = {}
        while start < end:
            sums = array[start] + array[end]
            if sums > tsum:
                end -= 1
                
            elif sums == tsum:
                pro = array[start] * array[end]
                result[pro] = [array[start], array[end]]
                start += 1
                end -= 1
            elif sums < tsum:
                start += 1

        if result != {}:
            return result[min(result.keys())]
        else:
            return []

if __name__ == '__main__':
    test = Solution()
    t = test.FindNumbersWithSum([1,2,4,7,11,15],15)
    print(t)
```





