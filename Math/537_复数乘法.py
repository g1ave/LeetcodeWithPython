# 复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：
#
# 实部 是一个整数，取值范围是 [-100, 100]
# 虚部 也是一个整数，取值范围是 [-100, 100]
# i2 == -1
# 给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/complex-number-multiplication
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Complex:
    def __init__(self, real: int, imaginary: int):
        self.real = real
        self.imaginary = imaginary

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real, imaginary)

    def __repr__(self):
        return f"{self.real}+{self.imaginary}i"

    def __str__(self):
        return f"{self.real}+{self.imaginary}i"


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, im1 = num1.split("+")
        real1 = int(real1)
        im1 = int(im1.strip("i"))
        real2, im2 = num2.split("+")
        real2 = int(real2)
        im2 = int(im2.strip("i"))
        return str(Complex(real1, im1) * Complex(real2, im2))


if __name__ == '__main__':
    s = Solution()

    print(s.complexNumberMultiply("1+-1i", "1+-1i"))
