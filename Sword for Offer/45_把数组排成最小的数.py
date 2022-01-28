# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# 0 < nums.length <= 100
import functools
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        str_nums = list(map(str, nums))
        str_nums.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(str_nums)


def quick_sort(left, right, arr):
    if left >= right:
        return
    i, j = left, right
    while i < j:
        while arr[j] >= arr[left] and i < j:
            j -= 1
        while arr[i] <= arr[left] and i < j:
            i += 1
        arr[i], arr[left] = arr[left], arr[i]

    quick_sort(left, i - 1, arr)
    quick_sort(j + 1, right, arr)


if __name__ == '__main__':
    s = Solution()
    nums = [10, 2, 5, 11, 9, 20]
    print(s.minNumber(nums))
    quick_sort(0, len(nums) - 1, nums)
    print(nums)
# 思路： 找所有数字中最高数位最小的，如果最高数位相同则比较第二高数位，以此类推，如果该数位上没有数字，则用前一位最小数字补（也对，但是难以实现）
# 题解： 自定义排序规则：if x + y < y + x, 则 x < y （x，y都为字符串）
# 知识点： 快排、Python中如何自定义排序函数、
