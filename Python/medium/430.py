# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/9/24 20:16
# version      : 3.7.2 


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node) -> Node:
        cur = head

        stack = []

        while cur:

            if cur.child:
                stack.append(cur.next)

                cur.next = cur.child
                cur.next.prev = cur
                cur.child = None

            elif not cur.next and len(stack)!=0:
                cur.next = stack.pop()
                cur.next.prev = cur

            cur = cur.next

        return head


