# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/11/18 22:32
# version      : 3.7.2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans

    def dfs(self, node: TreeNode) -> int:
        if node is None:
            return 0
        left_sum = self.dfs(node.left)
        right_sum = self.dfs(node.right)
        self.ans += abs(left_sum - right_sum)
        return left_sum + right_sum + node.val


if __name__ == '__main__':
    print(Solution().findTilt(TreeNode(5,)))