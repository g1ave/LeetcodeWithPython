# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
# 
# B是A的子结构， 即 A中有出现和B相同的结构和节点值。
# 
# 例如:
# 给定的树 A:
# 
#      3
#     / \
#    4   5
#   / \
#  1   2
# 给定的树 B：
# 
#    4 
#   /
#  1
# 返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        return bool(A and B) and (isTwoTreeEqual(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


def isTwoTreeEqual(A: TreeNode, B: TreeNode) -> bool:
    if not B:
        return True
    if A.val != B.val:
        return False
    return isTwoTreeEqual(A.left, B.left) and isTwoTreeEqual(A.right, B.right)


if __name__ == '__main__':
    l = [1, 3]
    l2 = [1, 3, 4]
    assert l == l2
