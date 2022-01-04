# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2022/1/4 22:07
# version      : 3.7.2

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: [TreeNode]) -> [int]:
        arr = []
        self.dfs(root, arr)
        return arr

    def dfs(self, root, arr):
        if root is None:
            return
        arr.append(root.val)
        self.dfs(root.left, arr)
        self.dfs(root.right, arr)


if __name__ == '__main__':
    print(Solution().preorderTraversal(TreeNode(5)))