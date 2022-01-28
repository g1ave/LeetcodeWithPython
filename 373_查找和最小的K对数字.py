# 给定两个以升序排列的整数数组 nums1 和 nums2,以及一个整数 k。
# 
# 定义一对值(u,v)，其中第一个元素来自nums1，第二个元素来自 nums2。
# 
# 请找到和最小的 k个数对(u1,v1), (u2,v2) ... (uk,vk)。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        ans = []
        i, j = 0, 0
        
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.kSmallestPairs([1, 7, 11], [2, 4, 6], 10))
    print(s.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
    print(s.kSmallestPairs([1, 2], [3], 3))

