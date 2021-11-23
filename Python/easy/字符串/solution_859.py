# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/11/23 21:18
# version      : 3.7.2


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        # TODO 这个地方存在问题，相同的情况下，要存在相同的一个字符才行
        if s == goal:
            if len(set(s)) < len(goal):
                return True
            else:
                return False

        index = []
        for idx in range(len(s)):
            if s[idx] != goal[idx]:
                index.append(idx)
        if len(index) == 2 and s[index[0]] == goal[index[1]] and s[index[1]] == goal[index[0]]:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().buddyStrings("aa", "aa"))
