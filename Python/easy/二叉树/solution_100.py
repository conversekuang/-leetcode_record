# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2022/1/4 22:11
# version      : 3.7.2

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.dfs(p, q)

    def dfs(self, p, q):
        if (q is None and p is not None) or (p is None and q is not None):
            return False
        elif q is None and p is None:
            return True
        elif p.val != q.val:
            return False
        else:
            return self.dfs(p.right, q.right) and self.dfs(p.left, q.left)


if __name__ == '__main__':
    print(Solution().isSameTree(TreeNode(5), TreeNode(5)))