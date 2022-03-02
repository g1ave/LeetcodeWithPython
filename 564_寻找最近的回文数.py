# 给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。
#
# “最近的”定义为两个整数差的绝对值最小。

# 1 <= n.length <= 18
# n 只由数字组成
# n 不含前导 0
# n 代表在 [1, 1018 - 1] 范围内的整数


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        candidates = [10 ** (m - 1) - 1, 10 ** m + 1]  # 考虑位数的变化
        selfPrefix = int(n[:(m + 1) // 2])  # 取前一半的值
        for x in range(selfPrefix - 1, selfPrefix + 2):
            y = x if m % 2 == 0 else x // 10  # 去掉最中间的一位
            while y:
                x = x * 10 + y % 10  # 将前面的数字镜像过来
                y //= 10
            candidates.append(x)

        ans = -1
        selfNumber = int(n)
        for candidate in candidates:  # 根据条件选取最近的回文数
            if candidate != selfNumber:
                if ans == -1 or \
                        abs(candidate - selfNumber) < abs(ans - selfNumber) or \
                        abs(candidate - selfNumber) == abs(ans - selfNumber) and candidate < ans:
                    ans = candidate

        return str(ans)


if __name__ == '__main__':
    s = Solution()
    assert s.nearestPalindromic("1") == "0"
    assert s.nearestPalindromic("123") == "121"
    assert s.nearestPalindromic("19") == "22"
    assert s.nearestPalindromic("39") == "44"
    assert s.nearestPalindromic("1234") == "1221"
    assert s.nearestPalindromic("999") == "1001"
    assert s.nearestPalindromic("1001") == "999"


# 思路：将后一半数字变为前一半数字的镜像
# 需要考虑边界问题：例如：12399
# 因此 将数字的前一半加一后镜像 已经减一后镜像
# 从中选择最接近的一个数字进行返回
# 数字的前一半+-1可能会导致数字位数变化 因此还需要构造临界值(99...99 或 100...001)进行判断 99...99 和 100...001


