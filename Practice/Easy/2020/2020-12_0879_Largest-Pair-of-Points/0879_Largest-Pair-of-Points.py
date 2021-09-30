import math

class Solution:
    def solve(self, nums, values):
        maxim = -math.inf
        dim = len(nums)
        max_sum = -math.inf
        for i in range(dim - 1, -1, -1):
            max_sum = max(max_sum, values[i] + nums[i])
            maxim = max(maxim, max_sum + values[i] - nums[i])
        return maxim
