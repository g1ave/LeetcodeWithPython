# 你正在参加一个多角色游戏，每个角色都有两个主要属性：攻击 和 防御 。给你一个二维整数数组 properties ，
# 其中 properties[i] = [attack_i, defense_i] 表示游戏中第 i 个角色的属性。
#
# 如果存在一个其他角色的攻击和防御等级 都严格高于 该角色的攻击和防御等级，则认为该角色为 弱角色 。更正式地，
# 如果认为角色 i 弱于 存在的另一个角色 j ，那么 attack_j > attack_i 且 defense_j > defense_i 。
#
# 返回 弱角色 的数量。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/the-number-of-weak-characters-in-the-game
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans, maxDefense = 0, 0
        for _, defense in properties:
            if defense < maxDefense:
                ans += 1
            else:
                maxDefense = defense
        return ans

# 思路：
# 1. 根据 attack 排序
# 2. 判断 defense 大小

# 题解：1. 根据 attack 从大到小排序
# 2. 遍历，记录当前 defense 的最大值 maxDefense，如果当前 maxDefense > defense， 则说明前面存在一个item强于当前角色
# 3. 但是题目要求是严格大于，所以在排序的时候采用，attack 从大到小的同时 相同attack从小到大，保证了 maxDefense > defense 时，
# attack 是不同的


if __name__ == '__main__':
    s = Solution()
    assert s.numberOfWeakCharacters([[5, 5], [6, 3], [3, 6]]) == 0
    assert s.numberOfWeakCharacters([[2, 2], [3, 3]]) == 1
    assert s.numberOfWeakCharacters([[1, 5], [10, 4], [4, 3]]) == 1
