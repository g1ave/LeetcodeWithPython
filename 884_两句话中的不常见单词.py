# 句子 是一串由空格分隔的单词。每个 单词 仅由小写字母组成。
#
# 如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 没有出现 ，那么这个单词就是 不常见的 。
#
# 给你两个 句子 s1 和 s2 ，返回所有 不常用单词 的列表。返回列表中单词可以按 任意顺序 组织。
#
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/uncommon-words-from-two-sentences
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import defaultdict
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        wordCounter = defaultdict(int)
        for word in s1.split() + s2.split():
            wordCounter[word] += 1

        return [item for item in wordCounter.keys() if wordCounter[item] == 1]

# 思路：题目相当于查找在 s1 + s2 中只出现了一次的单词


if __name__ == '__main__':
    s = Solution()
    assert s.uncommonFromSentences("this apple is sweet", "this apple is sour") == ["sweet", "sour"]
    assert s.uncommonFromSentences("apple apple", "banana") == ["banana"]
