class Solution:

    def intToRoman(self, num: int) -> str:
        roman_dict = {
            1000: 'M',
            100: 'C',
            10: 'X',
            1: 'I'
        }
        special_dict = {
            4: 'IV',
            5: 'V',
            9: 'IX',
            40: 'XL',
            50: 'L',
            90: 'XC',
            400: 'CD',
            500: 'D',
            900: 'CM'
        }
        ans = ''
        for i in roman_dict.keys():
            n = num // i
            if n in [4, 9]:
                ans += special_dict[n * i]
            elif n >= 5:
                ans += special_dict[i * 5] + (n - 5) * roman_dict[i]
            else:
                ans += roman_dict[i] * n
            num = num - n * i

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(2000))
    assert s.intToRoman(2000) == 'MM'
    print(s.intToRoman(1994))
    assert s.intToRoman(1994) == "MCMXCIV"
    print(s.intToRoman(1778))
