# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_value = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_value.append(min(x, self.min_value[-1]) if self.min_value else x)

    def pop(self) -> None:
        self.stack.pop()
        self.min_value.pop()

    def top(self) -> int:
        try:
            return self.stack[-1]
        except:
            return -1

    def min(self) -> int:
        return self.min_value[-1]
