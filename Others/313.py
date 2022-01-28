from typing import *


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ans = [1]
        pointers = [1] * len(primes)
        while len(ans) < n:
            current_ugly_num = min(primes[i] * ans[pointers[i] - 1] for i in range(len(primes)))
            ans.append(current_ugly_num)
            for i in range(len(pointers)):
                if primes[i] * ans[pointers[i] - 1] == current_ugly_num:
                    pointers[i] += 1
        return ans[-1]
