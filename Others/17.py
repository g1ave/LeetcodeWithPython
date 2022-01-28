from typing import List


class Solution:

    digit_to_letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def __init__(self):
        self.ans = []

    def letterCombinations(self, digits: str) -> List[str]:
        self.backtrace(digits, 0, '')
        return self.ans

    def backtrace(self, digits: str, index: int, prefix: str):
        if not digits:
            return
        if index == len(digits):
            self.ans.append(prefix)
            return
        for letter in self.digit_to_letters[digits[index]]:
            self.backtrace(digits, index + 1, prefix + letter)


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
    print(s.letterCombinations(''))



