# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/12/30 20:38
# version      : 3.7.2

class Solution:
    def search(self, nums: [int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            if nums[0] == target:
                return 0

        # 为什么忽略了=号？总会出现两个值相等的情况下
        while right >= left:
            mid = (left + right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    print(Solution().search([2,5],5))