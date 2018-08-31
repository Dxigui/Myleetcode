## 747. Largest Number At Least Twice of Others

 In a given integer array `nums`, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the **index** of the largest element, otherwise return -1.

**Example 1:**

```
Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
```

 

**Example 2:**

```
Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
```

 

**Note:**

1. `nums` will have a length in the range `[1, 50]`.
2. Every `nums[i]` will be an integer in the range `[0, 99]`.



思路:

1. 获取最大的值即索引,然后删除,在取删除后的最大值,对这两个值作比较
2. 取最大值,然后遍历列表,判断最大值和出本身外的其他数

```python
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        max_num = max(nums)
        index = nums.index(max_num)
        nums.remove(max_num)
        next_num = max(nums)
        if max_num >= next_num*2:
            return index
        else:
            return -1

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        for num in nums:
            if num*2 > max_num and num != max_num:
                return -1
        return nums.index(max_num)
```

