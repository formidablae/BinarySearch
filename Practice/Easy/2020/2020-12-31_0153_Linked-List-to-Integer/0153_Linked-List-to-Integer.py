# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        bits = ""
        while node is not None:
            bits += str(node.val)
            node = node.next
        return int(bits, 2)
        
