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


if __name__ == '__main__':
    s = Solution()
    assert s.reverseOnlyLetters("ab-cd") == "dc-ba"
