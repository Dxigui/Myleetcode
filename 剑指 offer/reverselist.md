## 反转链表

输入一个链表，反转链表后，输出新链表的表头。

代码:

```python
# -*- coding:utf-8 -*-
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        last = None
        while pHead:
            # 交换指针
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last
```

## 链表概念

链表是一种线性表,随机存储在物理内存中,每个节点都有指向下一个节点的指针(最后一个指向 `None`)每个节点包含**数据**和**指针**,插入O(1),读取O(n).

缺点:

* 由于指针使用内存,使用内存多余数组
* 读取时间长

### 单链表

单链表节点包含数据和指向下一节点的指针

### 循环链表

循环列表的最后一个节点的指针指向的是头节点

### 双向链表

双向链表的节点包含两个指针:前驱 `Prev` ,后继 `Next`,