import math

class Solution:
    def solve(self, nums, k):
        dim = len(nums)
        if k == 0:
            return max(nums) - min(nums)
        elif dim == 1 or k == dim - 1 or dim <= k:
            return 0
        else:
            maximums = {}
            minimums = {}
            maximums_fh = {}
            minimums_fh = {}
            maximums_sh = {}
            minimums_sh = {}
            maximums_fh[0] = -math.inf
            minimums_fh[0] = math.inf
            maximums_sh[dim - k] = -math.inf
            minimums_sh[dim - k] = math.inf
            # print("maximums", maximums)
            # print("minimums", minimums)
            # print("maximums_fh", maximums_fh)
            # print("minimums_fh", minimums_fh)
            # print("maximums_sh", maximums_sh)
            # print("minimums_sh", minimums_sh)
            expr = math.inf
            for i in range(dim - k):
                maximums_fh[i + 1] = max(nums[i], maximums_fh[i])
                minimums_fh[i + 1] = min(nums[i], minimums_fh[i])
                newindex = dim - k - i - 1
                maximums_sh[newindex] = max(nums[newindex + k], maximums_sh[newindex + 1])
                minimums_sh[newindex] = min(nums[newindex + k], minimums_sh[newindex + 1])
                # print("i", i, "dim", dim, "k", k, "newindex", newindex)
                # print("maximums", maximums)
                # print("minimums", minimums)
                # print("maximums_fh", maximums_fh)
                # print("minimums_fh", minimums_fh)
                # print("maximums_sh", maximums_sh)
                # print("minimums_sh", minimums_sh)
            maximums[0] = maximums_sh[0]
            minimums[0] = minimums_sh[0]
            maximums[dim - k] = maximums_fh[dim - k]
            minimums[dim - k] = minimums_fh[dim - k]
            expr = min(expr, maximums[0] - minimums[0])
            # print("expr", expr)
            expr = min(expr, maximums[dim - k] - minimums[dim - k])
            # print("expr", expr)
            for j in range(1, dim - k):
                maximums[j] = max(maximums_fh[j], maximums_sh[j])
                minimums[j] = min(minimums_fh[j], minimums_sh[j])
                expr = min(expr, maximums[j] - minimums[j])
                # print("j", j, "dim", dim, "k", k, "newindex", newindex)
                # print("maximums", maximums)
                # print("minimums", minimums)
                # print("expr", expr)
            return expr


# sl = Solution()
# inp1_int_list = [1, 2, 9, 8, 7, 3]
# inp1_int = 3
# print(sl.solve(inp1_int_list, inp1_int))