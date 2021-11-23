# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/11/20 15:28
# version      : 3.7.2


class Solution:
    def findLHS(self, nums: [int]) -> int:
        total = 0
        map_dict = {}
        for num in nums:
            if num in map_dict:
                map_dict[num] += 1
            else:
                map_dict[num] = 1

        for key, val in map_dict.items():
            if key+1 in map_dict:
                total = max(total, val + map_dict[key+1])

        return total


if __name__ == '__main__':
    print(Solution().findLHS([3,2,2,2,3]))