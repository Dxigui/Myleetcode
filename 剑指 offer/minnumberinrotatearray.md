## 旋转数组的最小数字

一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。



思路:

* 利用二分法从两侧开始找,会出现三种情况
* `Array[mid] < Array[left]`
* `Array[mid] == Array[left]`
* `Array[min] > Array[left]`



```python
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray == []:
            return 0
        left, right = 0, len(rotateArray) - 1
        while left < right:
            mid = (right + left) // 2
            if rotateArray[mid] > rotateArray[left]:
                left = mid + 1
            elif rotateArray[mid] == rotateArray[left]:
                left += 1
            else:
                right = mid
        return rotateArray[left]

if __name__ == '__main__':
    t = [2,3,4,5,6,6,6,6,1,2,2]
    test = Solution()
    te = test.minNumberInRotateArray(t)
    print(te)

```

