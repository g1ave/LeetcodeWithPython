# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
#
# 叶子节点 是指没有子节点的节点。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(root, target):
            if not root or root.val > target:
                return
            path.append(root.val)
            if root.val == target and not root.right and not root.left:
                ans.append(path[:])
                path.pop()
                return
            dfs(root.left, target - root.val)
            dfs(root.right, target - root.val)
            path.pop()

        dfs(root, target)
        return ans

# 思路：深度优先搜索，用一个list保存路径（即每次进入一个节点就添加该节点的值，搜索完左右子树或遇到解后pop）
# 遇到解就将遇到解时的路径添加到ans中 搜索完整棵树后返回ans


