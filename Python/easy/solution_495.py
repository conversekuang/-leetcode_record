#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: converse
@version: 1.0.0
@file: solution_495.py
@time: 2021/11/10 9:40
"""
class Solution:
    def findPoisonedDuration(self, timeSeries: [int], duration: int) -> int:
        duration_sum = 0
        end = 0
        flag = False
        for idx in range(len(timeSeries)):
            if flag == False:
                end = timeSeries[idx] + duration - 1
                duration_sum = duration
                flag = True
            else:
                if timeSeries[idx] > end:
                    duration_sum = duration_sum + duration
                else:
                    duration_sum = duration_sum + timeSeries[idx] - timeSeries[idx-1]
                end = timeSeries[idx] + duration
        return duration_sum


if __name__ == '__main__':
    print(Solution().findPoisonedDuration([1,2], 2))