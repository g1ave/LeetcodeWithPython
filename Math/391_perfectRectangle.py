# 给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi] 表示一个坐标轴平行的矩形。这个矩形的左下顶点是 (xi, yi) ，右上顶点是 (ai, bi) 。
#
# 如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/perfect-rectangle
from collections import defaultdict
from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        minX, minY, maxX, maxY = rectangles[0]
        area, points = 0, defaultdict(lambda: 0)
        for x1, y1, x2, y2 in rectangles:
            minX = min(minX, x1)
            minY = min(minY, y1)
            maxX = max(maxX, x2)
            maxY = max(maxY, y2)

            area += (y2 - y1) * (x2 - x1)
            points[(x1, y1)] += 1
            points[(x2, y1)] += 1
            points[(x1, y2)] += 1
            points[(x2, y2)] += 1

        if (maxY - minY) * (maxX - minX) != area:
            return False

        if points[(minX, minY)] != 1 or points[(minX, maxY)] != 1 or points[(maxX, minY)] != 1 or points[(maxX, maxY)] != 1:
            return False

        del points[(minX, minY)], points[(minX, maxY)], points[(maxX, minY)], points[(maxX, maxY)]

        return all(c == 2 or c == 4 for c in points.values())


if __name__ == '__main__':
    s = Solution()
    rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
    assert s.isRectangleCover(rectangles)
    rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [3, 2, 4, 4]]
    assert s.isRectangleCover(rectangles) is False
    rectangles = [[0, 0, 1, 1], [0, 1, 3, 2], [1, 0, 2, 2]]
    assert s.isRectangleCover(rectangles) is False

# 题解：若是完美矩形需要满足两个条件
# 1 小矩形的面积之和等于大矩形的面积
# 2 除了大矩形的四个顶点，其他顶点必定在同一位置出现两次或者四次 不然拼接不上
# 因此采用哈希表， 将每个位置上的顶点数存储起来同时计算小矩阵的面积和
