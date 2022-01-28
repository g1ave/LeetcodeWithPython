# 给你一个整数数组nums ，判断这个数组中是否存在长度为 3 的递增子序列。
# 
# 如果存在这样的三元组下标 (i, j, k)且满足 i < j < k ，使得nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/increasing-triplet-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import math
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        first, second = nums[0], math.inf
        for i in range(1, n):
            if nums[i] > second:
                return True
            elif nums[i] > first:
                second = nums[i]
            else:
                first = nums[i]
        return False

# 题解：从前往后遍历 维护两个数 始终保持 second > first 当遍历到第i个数时，如果nums[i] > second 则说明找到了 返回True
# 如果 first < nums[i] < second 则 second = nums[i]
# 如果 nums[i] < first, 则first = nums[i]
# 这样做可以使前面两个尽可能小 贪心思想


if __name__ == '__main__':
    s = Solution()
    assert s.increasingTriplet([1, 2, 3, 4, 5])
    assert s.increasingTriplet([5, 4, 3, 2, 1]) is False
    assert s.increasingTriplet([2, 1, 5, 0, 4, 6])
    assert s.increasingTriplet([0, 4, 2, 1, 0, -1, -3]) is False
    assert s.increasingTriplet([20, 100, 10, 12, 5, 13])
    assert s.increasingTriplet([1, 5, 0, 4, 1, 3])
