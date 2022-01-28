# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向
#  https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/

# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.head = None
        self.pre = None

    def treeToDoublyList(self, root: 'Node') -> Optional[None, Node]:
        # def dfs(root: Node):
        #     if not root:
        #         return []
        #     ans = []
        #     if root.left:
        #         ans += dfs(root.left)
        #     ans.append(root)
        #     if root.right:
        #         ans += dfs(root.right)
        #     return ans
        #
        # node_list = dfs(root)
        # head, n = node_list[0], len(node_list)
        # for i in range(n):
        #     node_list[i].right = node_list[(i+1) % n]
        #     node_list[i].left = node_list[i-1]
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            if not self.pre:
                self.head = cur
            else:
                self.pre.right, cur.left = cur, self.pre
            self.pre = cur
            dfs(cur.right)
        if not root:
            return None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

# 二叉搜索树： 左子树的值 < 根节点的值 < 右子树的值
# 想法：直接进行一次中序遍历，保存各个结点，然后进行链接
# 题解：在中序遍历的过程中用双指针进行链接
