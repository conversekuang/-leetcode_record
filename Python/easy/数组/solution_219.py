# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/12/28 22:05
# version      : 3.7.2


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_map = set()
        for idx in range(len(nums)):
            if nums[idx] in dict_map:
                return True
            dict_map.add(nums[idx])
            if len(dict_map) > k:
                dict_map.remove(nums[idx-k])
        return False

if __name__ == '__main__':
    print(Solution(object).containsNearbyDuplicate(nums =[99,99],k =2))