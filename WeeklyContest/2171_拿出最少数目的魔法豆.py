# 给你一个 正 整数数组 beans ，其中每个整数表示一个袋子里装的魔法豆的数目。
#
# 请你从每个袋子中 拿出 一些豆子（也可以 不拿出），使得剩下的 非空 袋子中（即 至少 还有 一颗 魔法豆的袋子）魔法豆的数目 相等 。一旦魔法豆从袋子中取出，你不能将它放到任何其他的袋子中。
#
# 请你返回你需要拿出魔法豆的 最少数目。

# 1 <= beans.length <= 10^5
# 1 <= beans[i] <= 10^5
from collections import defaultdict
from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        cnt = defaultdict(int)
        for bean in beans:
            cnt[bean] += 1
        cnt = sorted(cnt.items())
        ans = float("inf")
        totalBeans = sum(k * v for k, v in cnt)
        suffixTotal = []
        n = len(beans)
        for k, v in cnt:
            suffixTotal.append(n)
            n -= v
        for i, (k, v) in enumerate(cnt):
            ans = min(ans, totalBeans - suffixTotal[i] * k)

        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.minimumRemoval([4, 1, 6, 5]) == 4
    assert s.minimumRemoval([2, 10, 3, 2]) == 7
    assert s.minimumRemoval([2, 10, 3, 2, 3, 2]) == 10
    print(s.minimumRemoval([66, 90, 47, 25, 92, 90, 76, 85, 22, 3]))


# 思路：数学思路，寻找取出豆子数量最少时最终的豆子数x
# x 一定为初始时某个袋子中豆子数
# 先排序 然后从小到大判断一下就OK
