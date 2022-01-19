#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: converse
@version: 1.0.0
@file: solution_217.py
@time: 2022/1/19 9:25
"""


class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        dict_res = set()
        for idx in range(len(nums)):
            if nums[idx] in dict_res:
                return True
            else:
                dict_res.add(nums[idx])

        return False


if __name__ == '__main__':
    print(Solution().containsDuplicate([1,2,3]))