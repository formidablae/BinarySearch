class Solution:
    def solve(self, n):
        limit = n * 2 - 1
        if (limit + 1) % 4 == 0:
            return (limit + 1) * (limit + 1) // 4
        elif (limit + 1) % 4 == 1:
            return (limit * limit) // 4
        elif (limit + 1) % 4 == 2:
            return (limit - 1) * (limit + 1) // 4 + (limit + 1) // 2
        else:
            return (limit - 1) * n // 4
