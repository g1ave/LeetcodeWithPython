# 我们有n栋楼，编号从0到n - 1。每栋楼有若干员工。由于现在是换楼的季节，部分员工想要换一栋楼居住。
# 
# 给你一个数组 requests，其中requests[i] = [from_i, to_i]，表示一个员工请求从编号为from_i的楼搬到编号为to_i的楼。
# 
# 一开始所有楼都是满的，所以从请求列表中选出的若干个请求是可行的需要满足 每栋楼员工净变化为 0。意思是每栋楼 离开的员工数目 等于该楼 搬入的
# 员工数数目。比方说n = 3且两个员工要离开楼0，一个员工要离开楼1，一个员工要离开楼 2，如果该请求列表可行，应该要有两个员工搬入楼0，
# 一个员工搬入楼1，一个员工搬入楼2。
# 
# 请你从原请求列表中选出若干个请求，使得它们是一个可行的请求列表，并返回所有可行列表中最大请求数目。

# 1 <= n <= 20
# 1 <= requests.length <= 16
# requests[i].length == 2
# 0 <= from_i, to_i < n
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-number-of-achievable-transfer-requests
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import defaultdict
from typing import List
from itertools import combinations


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        for i in range(len(requests), 0, -1):
            selectedRequests = combinations(requests, i)
            for rq in selectedRequests:
                cnt = defaultdict(int)
                for from_i, to_i in rq:
                    cnt[from_i] -= 1
                    cnt[to_i] += 1
                flag = True
                for c in cnt.values():
                    if c != 0:
                        flag = False
                        break
                if flag:
                    ans = i
                    break
            if ans > 0:
                return ans
        return 0


if __name__ == '__main__':
    s = Solution()
    assert s.maximumRequests(5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]) == 5
    assert s.maximumRequests(3, [[1, 1]]) == 1

# 思路：当从每一栋楼搬出去的人数等于每一栋楼搬进去的人数时，请求成立
# 直接暴力，C_16^1 + C_16^2 + ... + C_16^16
# 从所有请求中从多到少组合请求，若能满足，则返回组合的请求数
# 有个坑，题目中没有明说 from_i != to_i 但是其实是可以相等的，即 可以从自己的楼换到自己的楼
