# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2022/1/5 20:11
# version      : 3.7.2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.dfs(root)

    def dfs(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            return max(self.dfs(root.left), self.dfs(root.right))+1


if __name__ == '__main__':
    print(Solution().maxDepth(TreeNode(12)))