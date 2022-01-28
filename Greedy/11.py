from typing import List


class Solution:

    # 方法一 暴力 把每两条线构成的容器容量都计算一下 选取最大的即可 (TLE)
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        capacity = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                capacity[i][j] = (j - i) * min(height[i], height[j])

        ans = 0
        for i in capacity:
            ans = max(max(i), ans)

        return ans

    # 方法二 找到两边最高的边界 (其实还是n ^ 2 只不过优化了一下 样本数据特别差的时候就会TLE)
    def max_area(self, height: List[int]) -> int:
        n = len(height)
        left_board = [(0, height[0])]
        max_left, max_right = height[0], height[n - 1]
        for index, h in enumerate(height):
            if h > max_left:
                max_left = h
                left_board.append((index, h))

        ans = 0
        for h in left_board:
            ans = max(ans, min(h[1], height[n - 1]) * (n - 1 - h[0]))

        for i in range(n - 1, 0, -1):
            if height[i] > max_right:
                max_right = height[i]
                for h in left_board:
                    if i > h[0]:
                        ans = max(ans, min(h[1], height[i]) * (i - h[0]))
        return ans

    # 方法3：双指针 向内收缩 保持高的一边不动 维护一个最大值即可
    def maxArea3(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        ans = 0
        while i < j:
            ans = max(ans, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert solution.max_area(heights) == 49
    assert solution.max_area([4, 4, 2, 11, 0, 11, 5, 11, 13, 8]) == 55
    assert solution.maxArea3(heights) == 49
