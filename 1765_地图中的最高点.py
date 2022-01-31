# 给你一个大小为 m x n 的整数矩阵 isWater ，它代表了一个由 陆地 和 水域 单元格组成的地图。
# 
# 如果 isWater[i][j] == 0 ，格子 (i, j) 是一个 陆地 格子。
# 如果 isWater[i][j] == 1 ，格子 (i, j) 是一个 水域 格子。
# 你需要按照如下规则给每个单元格安排高度：
# 
# 每个格子的高度都必须是非负的。
# 如果一个格子是是 水域 ，那么它的高度必须为 0 。
# 任意相邻的格子高度差 至多 为 1 。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。（也就是说它们有一条公共边）
# 找到一种安排高度的方案，使得矩阵中的最高高度值 最大 。
# 
# 请你返回一个大小为 m x n 的整数矩阵 height ，其中 height[i][j] 是格子 (i, j) 的高度。如果有多种解法，请返回 任意一个 。
# 
#  
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/map-of-highest-peak
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        ans = [[item - 1 for item in row] for row in isWater]
        q = deque((i, j) for i, row in enumerate(isWater) for j, water in enumerate(row) if water)
        while q:
            i, j = q.popleft()
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                print(x, y)
                if 0 <= x < m and 0 <= y < n and ans[x][y] == -1:
                    ans[x][y] = ans[i][j] + 1
                    q.append((x, y))
                    # print(q)
        return ans


# 思路：
# 1. 水域确定为 0
# 2. 水域周围只能是 1
# 3. 其它格子最高只能为 周围格子中最低的格子的高度+1

# 题解： 多源广搜

if __name__ == '__main__':
    s = Solution()
    print(s.highestPeak([[0, 1], [0, 0]]))
    # print(s.highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]))
