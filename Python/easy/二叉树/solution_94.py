# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2022/1/4 20:12
# version      : 3.7.2

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: [TreeNode]) -> [int]:
        self.arr = []
        self.dfs(root, self.arr)
        return self.arr

    def dfs(self, root, arr):
        if root is None:
            return

        self.dfs(root.left, arr)
        arr.append(root.val)
        self.dfs(root.right, arr)


if __name__ == '__main__':
    print(Solution().inorderTraversal(TreeNode(5)))