class Solution:
    def solve(self, nums):
        self = self
        started = False
        finnished = False
        for i in range(len(nums)):
            if finnished and nums[i] == 1:
                return False
            if nums[i] == 1 and not started:
                started = True
            elif nums[i] == 1 and started:
                pass
            elif nums[i] != 1 and not started:
                pass
            elif nums[i] != 1 and started:
                finnished = True
        return True


sl = Solution()
inp1_nums = [0, 1, 1, 1, 2, 3]
inp2_nums = [1, 1, 0, 1, 1]
print(sl.solve(inp1_nums))
print(sl.solve(inp2_nums))