# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        count = 0
        while node is not None:
            node = node.next
            count += 1
        return count
