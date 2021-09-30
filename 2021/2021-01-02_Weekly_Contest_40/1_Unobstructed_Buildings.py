class Solution:
    def solve(self, heights):
        self = self
        dim = len(heights)
        maxright = 0
        indexes = []
        for i in range(dim):
            if heights[dim - i - 1] > maxright:
                indexes.insert(0, dim - i - 1)
            maxright = max(maxright, heights[dim - i - 1])
        return indexes


sl = Solution()
inp1_int_list = [1, 5, 5, 2, 3]
inp2_int_list = [5, 4, 3, 2, 1]
inp3_int_list = [1, 1, 1, 1, 1]
print(sl.solve(inp1_int_list))
print(sl.solve(inp2_int_list))
print(sl.solve(inp3_int_list))