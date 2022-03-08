# 你和一群强盗准备打劫银行。给你一个下标从 0开始的整数数组security，其中security[i]是第 i天执勤警卫的数量。日子从 0开始编号。同时给你一个整数time。
# 
# 如果第 i天满足以下所有条件，我们称它为一个适合打劫银行的日子：
# 
# 第 i天前和后都分别至少有 time天。
# 第 i天前连续 time天警卫数目都是非递增的。
# 第 i天后连续 time天警卫数目都是非递减的。
# 更正式的，第 i 天是一个合适打劫银行的日子当且仅当：
# security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ...
# <= security[i + time - 1] <= security[i + time].
# 
# 请你返回一个数组，包含 所有 适合打劫银行的日子（下标从 0开始）。返回的日子可以 任意顺序排列。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-good-days-to-rob-the-bank
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import defaultdict
from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if n < time * 2:
            return []
        if time == 0:
            return list(range(n))

        cnt = 0
        temp = defaultdict(lambda: False)
        ans = []
        for i in range(1, n - time):
            if security[i - 1] >= security[i]:
                cnt += 1
                if cnt >= time:
                    temp[i] = True
            else:
                cnt = 0

        cnt = 0
        for i in range(n - 2, time - 1, -1):
            if security[i + 1] >= security[i]:
                cnt += 1
                if cnt >= time and temp[i]:
                    ans.append(i)
            else:
                cnt = 0
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.goodDaysToRobBank([1, 2, 5, 4, 1, 0, 2, 4, 5, 3, 1, 2, 4, 3, 2, 4, 8], 2))


# 思路：两次遍历 从前往后遍历， 遇到连续time个非递增的下标则储存起来 然后再从后往前遍历，遇到连续time个非递增的下标也储存起来，
# 最后求一下二者的重合下标
# 具体实现上可以在第二次遍历的时候直接判断当前节点是否为第一个列表中的下标 且可以使用hashmap减少查找时间

# 题解：动态规划
# 计算出第i天左边非递增的天数和右边非递减的天数，两个值同时>=time时即符合条件
# 具体求解时使用动态规划的思路，如果 security[i] <= security[i - 1] then left[i] = left[i - 1] + 1 否则 left[i] = 0
