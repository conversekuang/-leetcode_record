# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2022/1/13 21:48
# version      : 3.7.2
class Solution:
    def dominantIndex(self, nums: [int]) -> int:
        maximum = max(nums)
        index = None
        for idx, num in enumerate(nums):
            if num == maximum:
                index = idx
            else:
                if maximum < 2*num:
                    return -1
        return index


if __name__ == '__main__':
    print(Solution().dominantIndex([1, 2, 3, 4]))