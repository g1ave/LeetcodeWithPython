# 累加数 是一个字符串，组成它的数字可以形成累加序列。
#
# 一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
#
# 给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。
#
# 说明：累加序列里的数 不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/additive-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:

    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for secondStart in range(1, n - 1):
            if num[0] == '0' and secondStart != 1:
                break
            for secondEnd in range(secondStart, n - 1):
                if num[secondStart] == '0' and secondEnd != secondStart:
                    break
                if self.valid(secondStart, secondEnd, num):
                    return True
        return False

    def valid(self, secondStart: int, secondEnd: int, num: str) -> bool:
        n = len(num)
        firstStart, firstEnd = 0, secondStart - 1
        while secondEnd < n - 1:
            third = self.stringAdd(num, firstStart, firstEnd, secondStart, secondEnd)
            thirdStart = secondEnd + 1
            thirdEnd = secondEnd + len(third)
            if thirdEnd >= n or num[thirdStart: thirdEnd+1] != third:
                break
            if thirdEnd == n - 1:
                return True
            firstStart, firstEnd = secondStart, secondEnd
            secondStart, secondEnd = thirdStart, thirdEnd
        return False

    def stringAdd(self, s: str, firstStart: int, firstEnd: int, secondStart: int, secondEnd: int) -> str:
        third, carry, cur, base = [], 0, 0, ord('0')
        while firstEnd >= firstStart or secondEnd >= secondStart or carry != 0:
            cur = carry
            if firstEnd >= firstStart:
                cur += ord(s[firstEnd]) - base
                firstEnd -= 1
            if secondEnd >= secondStart:
                cur += ord(s[secondEnd]) - base
                secondEnd -= 1
            carry = cur // 10
            cur %= 10
            third.append(chr(cur + base))
        return ''.join(third[::-1])

# 题解：穷举前两个数，然后用字符串加法得到第三个数，判断字符串后面是否是第三个数
# 知识点：字符串加法


if __name__ == '__main__':
    s = Solution()
    # ans = s.isAdditiveNumber('112358')
    # print(ans)
    # print(s.isAdditiveNumber('120122436'))
    # print(s.isAdditiveNumber('112358'))
    print(s.isAdditiveNumber('12122436'))
