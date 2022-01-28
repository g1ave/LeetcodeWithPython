from typing import List


class Solution:

    # 方法一：如果每一行的第一个元素小于目标元素便对该行元素进行二分寻找target 复杂度 m * log(n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            if matrix[i][0] <= target:
                j, temp = 0, n - 1
                while j <= temp:
                    col_mid = (j + temp) // 2
                    if matrix[i][col_mid] == target:
                        return True
                    elif matrix[i][col_mid] < target:
                        j = col_mid + 1
                    else:
                        temp = col_mid - 1

        return False

    # 方法二：从右上角开始寻找 小于 target 则 行 + 1 大于则 列 - 1 （相当于一棵二叉搜索树）
    # 左下角同理

    def _searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n, i = len(matrix) - 1, len(matrix[0]) - 1, 0

        while i <= m and n:
            if matrix[i][n] < target:
                i += 1
            elif matrix[i][n] > target:
                n -= 1
            else:
                return True

        return False

