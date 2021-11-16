# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/11/16 21:34
# version      : 3.7.2
class Solution:
    def firstBadVersion(self, n, bad):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        result = n
        while left <= right:
            mid = (left + right)//2
            if self.isBadVersion(bad, mid):
                left = mid + 1
            else:
                result = mid
                right = mid - 1
        return result

    def isBadVersion(self, bad, mid):
        # 接口定义问题
        if mid < bad:
            return True
        else:
            return False

if __name__ == '__main__':
    print(Solution().firstBadVersion(5, 4))