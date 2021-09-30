class Solution:
    def solve(self, s):
        chars = set()
        for c in s:
            if c in chars:
                return False
            else:
                chars.add(c)
        return True
