# 给你一个下标从 0 开始的数组 nums ，该数组由 n 个正整数组成。
#
# 如果满足下述条件，则数组 nums 是一个 交替数组 ：
#
# nums[i - 2] == nums[i] ，其中 2 <= i <= n - 1 。
# nums[i - 1] != nums[i] ，其中 1 <= i <= n - 1 。
# 在一步 操作 中，你可以选择下标 i 并将 nums[i] 更改 为 任一 正整数。
#
# 返回使数组变成交替数组的 最少操作数 。
from collections import defaultdict
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # 统计奇偶位置上出现次数最多和第二多的数字
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        for index, num in enumerate(nums):
            if index % 2:
                cnt1[num] += 1
            else:
                cnt2[num] += 1
        oddMaxValue1, oddMaxValue2 = 0, 0
        oddMax1, oddMax2 = 0, 0
        evenMaxValue1, evenMaxValue2 = 0, 0
        evenMax1, evenMax2 = 0, 0
        for k, v in cnt1.items():
            if v > oddMaxValue1:
                oddMaxValue2, oddMaxValue1 = oddMaxValue1, v
                oddMax2, oddMax1 = oddMax1, k
            elif v > oddMaxValue2:
                oddMaxValue2, oddMax2 = v, k
        for k, v in cnt2.items():
            if v > evenMaxValue1:
                evenMaxValue2, evenMaxValue1 = evenMaxValue1, v
                evenMax2, evenMax1 = evenMax1, k
            elif v > evenMaxValue2:
                evenMaxValue2, evenMax2 = v, k
        if oddMax1 != evenMax1:
            return len(nums) - evenMaxValue1 - oddMaxValue1
        else:
            return len(nums) - max(evenMaxValue1 + oddMaxValue2, evenMaxValue2 + oddMaxValue1)


if __name__ == '__main__':
    s = Solution()
    print(s.minimumOperations([4, 4, 4, 4, 3, 4]))
