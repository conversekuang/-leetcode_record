# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/11/9 23:16
# version      : 3.7.2


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        index = right
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                index = mid
                break
            if mid * mid > x:
                if (mid-1)*(mid-1) < x:
                    index = mid-1
                    break
                else:
                    right = mid - 1
                    # index = right
            else:
                left = mid + 1
                # index = left
        return index

if __name__ == '__main__':
    print(Solution().mySqrt(18))