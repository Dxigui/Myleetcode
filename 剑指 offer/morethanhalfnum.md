## 数组中出现次数超过一半的数字

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。



思路一(hashmap)

* 讲对应的值和出现的次数通过 `key-value` 存储在字典中
* 然后再判断数字是否超过一半

```python
# -*- coding:utf-6 -*-
class Solution(object):
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        
        length = len(numbers)
        if length < 1:
            return 0
        dict_index = {}
        count = 0
        for index,num in enumerate(numbers):
            rel = dict_index.get(num)
            if not rel:
                dict_index[num] = 1
            else:
                dict_index[num] += 1
        for key,value in dict_index.items():
            if value > length / 2:
                return key
        return 0

if __name__ == '__main__':
    array = [1,2,4,5,6,7,7,7,6,5,7,7,7,7,7,7,7]
    test = Solution()
    t = test.MoreThanHalfNum_Solution(array)
    print(t)                                                         1,18       

```

思路二

* 先排序(快排)
* 然后判断数组中间值和右边第一个是否相等 `Array[middle] == Array[minddle + 1]`

思路三

* 如果有符合条件的数字，则它出现的次数比其他所有数字出现的次数和还要多
* 在遍历数组时保存两个值：一是数组中一个数字，一是次数。遍历下一个数字时，若它与之前保存的数字相同，则次数加1，否则次数减1；若次数为0，则保存下一个数字，并将次数置为1。遍历结束后，所保存的数字即为所求。然后再判断它是否符合条件即可。