from collections import defaultdict
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        theNextBigNumber, stack = {}, []
        for num in reversed(nums2):
            while stack and stack[-1] < num:
                stack.pop()
            theNextBigNumber[num] = stack[-1] if stack else -1
            stack.append(num)
        return [theNextBigNumber[i] for i in nums1]


if __name__ == '__main__':
    s = Solution()
    a = s.nextGreaterElement([4,1,2], [1,3,4,2])
    print(a)


