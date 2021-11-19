#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: converse
@version: 1.0.0
@file: solution_397.py
@time: 2021/11/19 15:08
"""
class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = self.dfs(n, 0)
        return ans

    def dfs(self, n, total):
        if n == 1:
            return 0
        if n % 2 == 0:
            total = self.dfs(n//2, total)
            total += 1
        else:
            add = self.dfs(n + 1, total)
            minus = self.dfs(n - 1, total)
            total = min(add, minus)
            total += 1
        return total


if __name__ == '__main__':
    print(Solution().integerReplacement(4))