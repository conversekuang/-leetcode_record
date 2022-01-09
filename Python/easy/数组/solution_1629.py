# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2022/1/9 22:14
# version      : 3.7.2


class Solution:
    def slowestKey(self, releaseTimes: [int], keysPressed: str) -> str:
        key = None
        duration = 0
        LongestDur = 0
        LongestDurKey = 0
        for idx in range(len(releaseTimes)):
            if idx == 0:
                duration = releaseTimes[idx]
                key = keysPressed[idx]
                LongestDur = duration
                LongestDurKey = key
            else:
                duration = releaseTimes[idx] - releaseTimes[idx-1]
                key = keysPressed[idx]

                if duration > LongestDur:
                    LongestDurKey = key
                    LongestDur = duration

                elif duration == LongestDur:
                    if key > LongestDurKey:
                        LongestDurKey = key
                        LongestDur = duration
                else:
                    pass

        return LongestDurKey


if __name__ == '__main__':
    print(Solution().slowestKey([28,65,97], "gaf"))