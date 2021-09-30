class Solution:
    def solve(self, nums):
        if len(nums) < 2: return True
        elif len(nums) == 2 and nums[0] != nums[1]: return True
        elif nums[0] < nums[1]:
            for i in range(2, len(nums)):
                if not nums[i - 1] < nums[i]: return False
            return True
        elif nums[0] > nums[1]:
            for i in range(2, len(nums)):
                if not nums[i - 1] > nums[i]: return False
            return True
        else: return False
