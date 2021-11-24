# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/11/24 20:54
# version      : 3.7.2

from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        c = {}
        for idx in range(len(s)):
            char = s[idx]
            if char in c:
                c[char] +=1
            else:
                c[char] = 1
        c = Counter(s)

        cnt = [0] * 10
        cnt[0] = c.get("z", 0)
        cnt[2] = c.get("w", 0)
        cnt[4] = c.get("u", 0)
        cnt[6] = c.get("x", 0)
        cnt[8] = c.get("g", 0)

        cnt[3] = c.get("h", 0) - cnt[8]
        cnt[5] = c.get("f", 0) - cnt[4]
        cnt[7] = c.get("s", 0) - cnt[6]

        cnt[1] = c.get("o", 0) - cnt[0] - cnt[2] - cnt[4]

        cnt[9] = c.get("i", 0) - cnt[5] - cnt[6] - cnt[8]

        return "".join(str(x) * cnt[x] for x in range(10))

    # counter 用法
    def originalDigits1(self, s: str) -> str:
        c = Counter(s)
        cnt = [0] * 10
        cnt[0] = c["z"]
        cnt[2] = c["w"]
        cnt[4] = c["u"]
        cnt[6] = c["x"]
        cnt[8] = c["g"]

        cnt[3] = c["h"] - cnt[8]
        cnt[5] = c["f"] - cnt[4]
        cnt[7] = c["s"] - cnt[6]

        cnt[1] = c["o"] - cnt[0] - cnt[2] - cnt[4]

        cnt[9] = c["i"] - cnt[5] - cnt[6] - cnt[8]

        return "".join(str(x) * cnt[x] for x in range(10))


if __name__ == '__main__':
    print(Solution().originalDigits("owoztneoer"))
    print(Solution().originalDigits1("owoztneoer"))