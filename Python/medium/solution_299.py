# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/11/8 22:08
# version      : 3.7.2

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        secret_set = {str(i): 0 for i in range(10)}
        guess_set = {str(i): 0 for i in range(10)}
        for index in range(len(secret)):
            secret_set[secret[index]] += 1

        for index in range(len(guess)):
            guess_set[guess[index]] += 1

        for i in range(10):
            tmp_min = min(secret_set[str(i)], guess_set[str(i)])
            cow += tmp_min

        for idx in range(len(guess)):
            if secret[idx] == guess[idx]:
                bull += 1

        return "{}A{}B".format(bull, cow-bull)

if __name__ == '__main__':
    print(Solution().getHint("1807", "7810"))