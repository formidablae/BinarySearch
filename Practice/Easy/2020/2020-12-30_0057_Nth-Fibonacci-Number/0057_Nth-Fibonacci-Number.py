class Solution:
    def solve(self, n):
        if n < 3:
            return 1
        else:
            prev = 1
            actual = 1
            count = 2
            while count < n:
                prev, actual = actual, prev + actual
                count += 1
            return actual
