# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/11/15 22:01
# version      : 3.7.2

class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        left = 0
        right = len(numbers) - 1

        while True:
            if numbers[left] + numbers[right] == target:
                break
            elif numbers[left] + numbers[right] > target:
                right = right - 1
            else:
                left = left + 1

        return left+1, right+1


"""
二分法加双指针
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0, j = numbers.length - 1;
        while (i < j) {
            int m = (i + j) >>> 1;
            if (numbers[i] + numbers[m] > target) {
                j = m - 1;
            } else if (numbers[m] + numbers[j] < target) {
                i = m + 1;
            } else if (numbers[i] + numbers[j] > target) {
                j--;
            } else if (numbers[i] + numbers[j] < target) {
                i++;
            } else {
                return new int[]{i + 1, j + 1};
            }
        }
        return new int[]{0, 0};
    }
}

"""


if __name__ == '__main__':
    print(Solution().twoSum([3, 24, 50, 79, 88, 150, 345], 200))