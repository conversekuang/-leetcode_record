# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/11/4 21:17
# version      : 3.7.2
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        left = 0
        right = len(nums)-1
        index = len(nums)
        while left <= right:
            # 「在一个有序数组中找第一个大于等于 target 的下标」
            mid = (right+left)//2
            if target <= nums[mid]:
                index = mid
                right = mid - 1
            else:
                left = mid + 1

        return index


if __name__ == '__main__':
    print(Solution().searchInsert([1,3,5,6],7))