# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/9/26 20:38
# version      : 3.7.2 

class Solution {
    public int getSum(int a, int b) {
        while (b!=0){
            int carry = (a & b) << 1;
            a = a^b;
            b = carry;
        }
        return a;

    }
}