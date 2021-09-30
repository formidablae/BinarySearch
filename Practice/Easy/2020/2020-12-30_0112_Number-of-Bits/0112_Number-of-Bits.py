class Solution:
    def solve(self, n):
        str_bin_n = str(bin(n))
        length = len(str_bin_n)
        return sum([int(x) for x in str_bin_n[2:length]])
