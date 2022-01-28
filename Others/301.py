from typing import List


class Solution:
    def __init__(self):
        self.ans = set()

    def removeInvalidParentheses(self, s: str) -> List[str]:
        l, r = 0, 0
        for char in s:
            if char == "(":
                l += 1
            elif char == ")":
                if l > 0:
                    l -= 1
                else:
                    r += 1

        self.backtrace(s, 0, l, r, 0, 0, "")
        return list(self.ans)

    def backtrace(self, s: str, index: int, l: int, r: int, lcnt: int, rcnt: int, prefix: str):
        if index == len(s):
            if l == 0 and r == 0:
                self.ans.add(prefix)
            return

        # 删除当前位置的字符
        if s[index] == "(" and l > 0:
            self.backtrace(s, index + 1, l - 1, r, lcnt, rcnt, prefix)

        if s[index] == ")" and r > 0:
            self.backtrace(s, index + 1, l, r - 1, lcnt, rcnt, prefix)

        # 保留当前位置的字符
        prefix += s[index]

        if s[index] not in ["(", ")"]:
            self.backtrace(s, index + 1, l, r, lcnt, rcnt, prefix)
        elif s[index] == "(":
            self.backtrace(s, index + 1, l, r, lcnt + 1, rcnt, prefix)
        elif rcnt < lcnt:
            self.backtrace(s, index + 1, l, r, lcnt, rcnt + 1, prefix)


if __name__ == '__main__':
    ans = Solution().removeInvalidParentheses("(a)())()")
    print(ans)
