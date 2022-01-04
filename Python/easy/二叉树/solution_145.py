# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2022/1/4 22:10
# version      : 3.7.2

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: [TreeNode]) -> [int]:
        arr = []
        self.dfs(root, arr)
        return arr

    def dfs(self, root, arr):
        if root is None:
            return

        self.dfs(root.left, arr)
        self.dfs(root.right, arr)
        arr.append(root.val)


if __name__ == '__main__':
    print(Solution().postorderTraversal(TreeNode(5)))