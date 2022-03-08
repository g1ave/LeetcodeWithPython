class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        a = list(s)
        i, j = 0, len(a) - 1
        while i < j:
            if not a[i].isalpha():
                i += 1
            elif not a[j].isalpha():
                j -= 1
            else:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        return ''.join(a)


# 504 给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

class Solution1:
    def convertToBase7(self, num: int) -> str:
        temp = abs(num)
        ans = ''
        while temp > 0:
            ans += str(temp % 7)
            temp = temp // 7
        ans = ans[::-1]
        return ans if num >= 0 else '-' + ans


if __name__ == '__main__':
    s = Solution()
    assert s.reverseOnlyLetters("ab-cd") == "dc-ba"
