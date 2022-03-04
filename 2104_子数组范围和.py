# 给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。
#
# 返回 nums 中 所有 子数组范围的 和 。
#
# 子数组是数组中一个连续 非空 的元素序列。
#
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sum-of-subarray-ranges
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 1 <= nums.length <= 1000
# -10^9 <= nums[i] <= 10^9


from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 1):
            maxValue, minValue = nums[i], nums[i]
            for j in range(i + 1, n):
                maxValue = max(maxValue, nums[j])
                minValue = min(minValue, nums[j])
                ans += maxValue - minValue
        return ans

    def _subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        minLeft, maxLeft = [0] * n, [0] * n
        minStack, maxStack = [], []
        for i, num in enumerate(nums):
            while minStack and nums[minStack[-1]] > num:
                minStack.pop()
            minLeft[i] = minStack[-1] if minStack else -1
            minStack.append(i)

            while maxStack and nums[maxStack[-1]] <= num:
                maxStack.pop()
            maxLeft[i] = maxStack[-1] if maxStack else -1
            maxStack.append(i)

        minRight, maxRight = [0] * n, [0] * n
        minStack, maxStack = [], []

        for i in range(n - 1, -1, -1):
            num = nums[i]
            while minStack and nums[minStack[-1]] >= num:
                minStack.pop()
            minRight[i] = minStack[-1] if minStack else n
            minStack.append(i)

            while maxStack and nums[maxStack[-1]] < num:
                maxStack.pop()
            maxRight[i] = maxStack[-1] if maxStack else n
            maxStack.append(i)

        maxSum, minSum = 0, 0
        for i, num in enumerate(nums):
            maxSum += (maxRight[i] - i) * (i - maxLeft[i]) * num
            minSum += (minRight[i] - i) * (i - minLeft[i]) * num

        return maxSum - minSum


if __name__ == '__main__':
    s = Solution()
    assert s.subArrayRanges([1, 2, 3]) == 4
    assert s.subArrayRanges([1, 3, 3]) == 4
    assert s.subArrayRanges([4, -2, -3, 4, 1]) == 59

# 思路：1. 暴力 O(n^2)
# 2. 单调栈 O(n) 考虑每个数字是所有组合中最大值次数（i）和最小值的次数（j）
# ans = sum((i - j) * num for num in nums)
# 在考虑第i个数字的最大值次数时，以左边第一个比它大的值为左边界 l（但不包含），右边第一个比它大的值为右边界 r （也不包含）
# 那么最大值的次数为 (r-i) * (i-l)) 简单的排列组合
# 最小值的次数同理，以左边第一个比它小的数为左边界，右边第一个比他小的数做右边界
# 具体实现上需要使用四个单调栈来分别存储左边和右边最近的最大值、最小值的下标
# 左边最近的最大值最小值的下标从左到右遍历
# 右边最近的最大、小值下标从右到左遍历
# 且为了避免重复计算，应该在逻辑上认为 当 nums[i] == nums[j] 时， if i < j, then nums[i] < nums[j]
# 进阶要求 O(n) 只能用方法二
