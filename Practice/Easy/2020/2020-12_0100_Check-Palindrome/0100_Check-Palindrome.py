class Solution:
    def solve(self, s):
        dim = len(s)
        for i in range(dim // 2):
            if s[i] != s[dim - i - 1]:
                return False
        return True
