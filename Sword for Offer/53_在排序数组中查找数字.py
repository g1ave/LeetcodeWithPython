# 统计一个数字在排序数组中出现的次数。
from collections import defaultdict
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = defaultdict(int)
        return sum(1 if num == target else 0 for num in nums)