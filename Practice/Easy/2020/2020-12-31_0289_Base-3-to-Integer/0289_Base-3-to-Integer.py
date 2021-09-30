class Solution:
    def solve(self, s):
        dec = 0
        dim = len(s)
        for i in range(dim):
            bit = int(s[dim - i - 1])
            dig = bit * (3 ** i)
            dec += dig
        return dec

