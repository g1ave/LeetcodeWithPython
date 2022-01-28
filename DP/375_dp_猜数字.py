# 我们正在玩一个猜数游戏，游戏规则如下：
#
# 我从 1 到 n 之间选择一个数字。
# 你来猜我选了哪个数字。
# 如果你猜到正确的数字，就会 赢得游戏 。
# 如果你猜错了，那么我会告诉你，我选的数字比你的 更大或者更小 ，并且你需要继续猜数。
# 每当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。如果你花光了钱，就会 输掉游戏 。
# 给你一个特定的数字 n ，返回能够 确保你获胜 的最小现金数，不管我选择那个数字 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/guess-number-higher-or-lower-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        f = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1, 0, -1):
            for j in range(i + 1, n + 1):
                f[i][j] = min(k + max(f[i][k-1], f[k+1][j]) for k in range(i, j))
        return f[1][n]

# 题解：DP f[i][j] 表示从 i 到 j 的最多花费
# 选定 i j 之间的一个数 k，那么 f[i][j] = max(f[i][k-1], f[k+1][j]) + k
# 此外要遍历 i j 之间的所有数取最小值
