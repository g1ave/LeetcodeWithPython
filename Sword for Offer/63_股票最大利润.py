# 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = 10 ** 9
        maxProfit, minPrice = 0, inf
        for p in prices:
            maxProfit = max(maxProfit, p - minPrice)
            minPrice = min(minPrice, p)
        return maxProfit

# 思路：找到最低点，然后在最高点卖出
# 动态规划不一定维护一个数组
