##867. Transpose Matrix

Given a matrix `A`, return the transpose of `A`.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

 

**Example 1:**

```
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```

**Example 2:**

```
Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
```

 

**Note:**

1. `1 <= A.length <= 1000`
2. `1 <= A[0].length <= 1000`

思路:

* 输入矩阵的列数决定输出矩阵的行数

* 输入矩阵的行数决定输出矩阵的列数

```python
# 按照思路写第一种解法
def transpose(A):
    transpose_A = []
    for i in range(len(A[0])):
        L = []
        for j in range(lend(A)):
            L.append(j)
        transpose_A.append(L)
    return transpose_A
```

优化:

在 Python 中如果需要通过 for 循环来生成一个列表,那么就可以使用列表推导式来进行优化.

```python
# one line
def transpose(A):
	return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

```

