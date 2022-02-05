# 你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。
# 
# 为了使收益最大化，矿工需要按以下规则来开采黄金：
# 
# 每当矿工进入一个单元，就会收集该单元格中的所有黄金。
# 矿工每次可以从当前位置向上下左右四个方向走。
# 每个单元格只能被开采（进入）一次。
# 不得开采（进入）黄金数目为 0 的单元格。
# 矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。
# 1 <= grid.length, grid[i].length <= 15
# 0 <= grid[i][j] <= 100
# 最多 25 个单元格中有黄金。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-with-maximum-gold
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def traceback(i, j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] == 0:
                return 0
            cur = grid[i][j]
            grid[i][j] = 0
            v = cur + max(traceback(i + 1, j), traceback(i - 1, j), traceback(i, j - 1), traceback(i, j + 1))
            grid[i][j] = cur
            return v

        maxValue = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] != 0:
                    maxValue = max(maxValue, traceback(x, y))
        return maxValue


# 思路：直接对于每一个不为空的格子进行深搜
# 搜索所有可能，记录最大值
# 最后取所有格子的最大值

if __name__ == '__main__':
    s = Solution()
    assert s.getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]) == 24
    assert s.getMaximumGold([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]) == 28
