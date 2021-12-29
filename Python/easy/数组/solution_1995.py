# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/12/29 21:42
# version      : 3.7.2


class Solution:
    def countQuadruplets(self, nums: [int]) -> int:
        n =  len(nums)
        ans = 0
        for a in range(n):
            for b in range(a+1, n):
                for c in range(b+1, n):
                    for d in range(c+1, n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            ans += 1
        return ans

if __name__ == '__main__':
    print(Solution().countQuadruplets([1,2,3,6]))