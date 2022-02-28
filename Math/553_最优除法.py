# 给定一组正整数，相邻的整数之间将会进行浮点除法操作。例如，[2,3,4] -> 2 / 3 / 4 。
#
# 但是，你可以在任意位置添加任意数目的括号，来改变算数的优先级。你需要找出怎么添加括号，才能得到最大的结果，并且返回相应的字符串格式的表达式。你的表达式不应该含有冗余的括号。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/optimal-division
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 说明:
#
# 输入数组的长度在 [1, 10] 之间。
# 数组中每个元素的大小都在 [2, 1000] 之间。
# 每个测试用例只有一个最优除法解。

from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])

        if len(nums) == 2:
            return "/".join(str(num) for num in nums)

        return f"{nums[0]}/(" + "/".join(str(num) for num in nums[1:]) + ")"


# 思路：要使商最大 则需使被除数尽可能大 以及除数尽可能小
# 由于数组中每个元素的大小都 > 2
# 因此只需要在第二个数字和最后一个数字之间加上()
