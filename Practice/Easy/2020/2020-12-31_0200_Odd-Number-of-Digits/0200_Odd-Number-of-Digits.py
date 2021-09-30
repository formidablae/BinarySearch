class Solution:
    def solve(self, nums):
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 1:
                count += 1
        return count
