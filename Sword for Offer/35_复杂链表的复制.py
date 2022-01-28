# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
#
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        node_list, cur = [], head
        while cur:
            node_list.append(cur)
            cur = cur.next
        new_head = Node(x=head.val, next=head.next, random=head.random)
