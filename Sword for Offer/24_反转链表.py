# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        node_stack = []
        while head:
            node_stack.append(head)
            head = head.next
        new_head = node_stack.pop()
        cur = new_head
        while node_stack:
            cur.next = node_stack.pop()
            cur = cur.next
        cur.next = None
        return new_head
