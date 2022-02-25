# 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。
#
# 给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：
#
# s 是一个尽可能长的快乐字符串。
# s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
# s 中只含有 'a'、'b' 、'c' 三种字母。
# 如果不存在这样的字符串 s ，请返回一个空字符串 ""。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-happy-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 0 <= a, b, c <= 100
# a + b + c > 0

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            cnt.sort(key=lambda x: -x[0])
            hasNext = False
            for i, (c, ch) in enumerate(cnt):
                if c <= 0:
                    break
                if len(ans) >= 2 and ans[-2] == ch and ans[-1] == ch:
                    continue
                hasNext = True
                ans.append(ch)
                cnt[i][0] -= 1
                break
            if not hasNext:
                return ''.join(ans)

# 思路：感觉是一种贪心
# 要想使字符串尽可能长且要避免出现 aaa bbb ccc
# 那么应该使用可以出现次数最多的字符先进行填充，然后用其它字符进行'分隔'
# 贪心的策略思考正确了但是代码上差太多了


if __name__ == '__main__':
    s = Solution()
    assert s.longestDiverseString(7, 1, 0) == "aabaa"
