# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/9/22 22:55
# version      : 3.7.2 


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> [ListNode]:
        node = head
        count = 0
        while node:
            node = node.next
            count += 1

        index = count // k
        res = count % k

        result = []

        numbers = [index for i in range(k)]
        for i in range(res):
            numbers[i] += 1

        node = head

        for i in numbers:
            if node is None:
                result.append(node)
            else:
                result.append(node)
                last = None
                while i != 0:
                    last = node
                    node = node.next
                    i = i - 1
                last.next = None

        return result
