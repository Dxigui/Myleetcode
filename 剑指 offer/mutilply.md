## 构建乘积数组

给定一个数组 `A[0,1,...,n-1]`,请构建一个数组 `B[0,1,...,n-1]`,其中B中的元素 `B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]`。不能使用除法。



思路:

* 根据题意 `B[i]` 为 去掉 `A[i]` 后的乘积,所以可以设 `B[i] == 1`
* 然后以 `B[i]` 为分界,分别求 `B[i]` 左右两侧的乘积,然后再将两侧相乘

| b[0]   | 1    | a[1] | ...  | a[n-2] | a[n-1] |
| ------ | ---- | ---- | ---- | ------ | ------ |
| b[1]   | a[0] | 1    | ...  | a[n-2] | a[n-1] |
| ...    | a[0] | a[1] | 1    | a[n-2] | a[n-1] |
| b[n-2] | a[0] | a[1] | ...  | 1      | a[n-1] |
| b[n-1] | a[0] | a[1] | ...  | a[n-2] | 1      |







```python
class Solution:
    def multiply(self, A):
        # write code here
        left = [1]
        right = [1]
        for i in range(len(A)-1):
            # 计算 B[i] 左边的值
            left.append(left[i]*A[i])
            # 计算 B[i] 右边的值
            # right.append(right[i]*A[-i-1])
            right.insert(0, right[-i-1]*A[-i-1])
        print(left,right)
        # return [left[j]*right[-j-1] for j in range(len(left))]
        return [left[j]*right[j] for j in range(len(left))]

if __name__ == '__main__':
    A = [1,2,3,4,5,6]
    test = Solution()
    t = test.multiply(A)
    print(t)
```

