# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        else:
            ans = self.reversePrint(head.next)
            ans.append(head.val)
        return ans
