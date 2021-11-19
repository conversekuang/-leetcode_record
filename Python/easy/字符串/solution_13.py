# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/11/17 21:08
# version      : 3.7.2

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = dic[s[-1]] # 初始化第一个就是加，最右边

        for idx in range(len(s) - 1, 0, -1):
            cur = dic[s[idx]]
            next = dic[s[idx - 1]]
            if next >= cur:
                total += next
            else:
                total -= next
        return total


# 主要是思路，从右到左。下一个比当前大就加，比当前小就减。


if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCIV"))
