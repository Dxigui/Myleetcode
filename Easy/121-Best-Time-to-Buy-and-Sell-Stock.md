## 121. Best Time to Buy and Sell Stock

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

**Example 1:**

```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

**Example 2:**

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

思路:

* 使用贪婪算法,假设第 i 轮卖出,买入在 i 之前且价格最低

```python
def maxProfit(prices):
    length = len(prices)
    if length == 0:
        return 0
    min_price = prices[0]
    max_price = 0
    for i in range(1,length):
        min_price = min(min_price, prices[i])
        max_price = max(prices[i], prices[i] - min_price)
    return max_price

if __name__ == '__main__':
    print(maxProfit([5,3,5,4,3,1,7,4,8,9]))
```

