# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/11/1 23:08
# version      : 3.7.2


class Solution:
    def distributeCandies(self, candyType) -> int:
        if len(set(candyType)) > len(candyType)/2:
            return int(len(candyType)//2)
        else:
            return len(set(candyType))


if __name__ == '__main__':
    candyType = [1,2,3,1,2]
    Solution().distributeCandies(candyType)