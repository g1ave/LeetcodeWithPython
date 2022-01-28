from typing import List


class Solution:

    def __init__(self):
        self.ans = []

    def addOperators(self, num: str, target: int) -> List[str]:
        self.search(num, target, "", 0)
        return self.ans

    def search(self, num: str, target: int, prefix: str, preNum: int):
        n = len(num)
        if n <= 1:
            return num
        if target > int(num):
            return num
        num1, num2 = int(num[:n - 1]), int(num[-1])
        if num1 + num2 == target:
            self.ans.append(f"{num1}+{num2}{prefix}")
        if num1 - num2 == target:
            self.ans.append(f"{num1}-{num2}{prefix}")
        if num1 * num2 == target:
            self.ans.append(f"{num1}*{num2}{prefix}")
        if num2 and target % num2 == 0:
            self.search(num[:-1], target // num2, f"*{num2}")
        self.search(num[:-1], target + num2, f"-{num2}")
        self.search(num[:-1], target - num2, f"+{num2}")


if __name__ == '__main__':
    print(Solution().addOperators("00", 0))
    print(Solution().addOperators("232", 8))
