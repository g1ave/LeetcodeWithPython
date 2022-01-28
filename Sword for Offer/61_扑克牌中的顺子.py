# 从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，
# 而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        cnt, i = 0, 0
        for num in nums:
            if num == 0:
                cnt += 1
        n = 4 - cnt
        while i < n:
            if nums[i] - 1 != nums[i + 1]:
                if cnt == 0:
                    return False
                else:
                    cnt, nums[i] = cnt - 1, nums[i] - 1
            else:
                i += 1
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.isStraight([0, 0, 2, 2, 5]) is False
    assert s.isStraight([1, 2, 3, 4, 5])
    assert s.isStraight([0, 0, 1, 2, 5])
# 思路：除去0数组里最大值-最小值 < 5 (错误,忽略了重复值 [0, 0, 2, 2, 5])
# 思路：排序后看每两个相邻的数字相差是否为1
# 题解：除去0数组里最大值-最小值 < 5 且不重复
