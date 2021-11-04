# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/11/4 20:40
# version      : 3.7.2
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left = 1
        right = num
        mid = (left+right)//2
        flag = False
        # 等号这里错了一次
        while left <= right:
            if mid**2 == num:
                flag = True
                break
            elif mid**2 > num:
                # -1这里错了一次
                right = mid-1
                mid = (left+right)//2
            else:
                # +1
                left = mid+1
                mid = (left+right)//2
        return flag


if __name__ == '__main__':
    print(Solution().isPerfectSquare(16))