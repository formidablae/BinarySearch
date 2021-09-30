class Solution:
    def solve(self, nums, k):
        length = len(nums)
        betternums = []
        for i in range(length):
            number = nums[i]
            if number not in betternums:
                betternums.append(number)
                if nums.count(number) > 1:
                    betternums.append(number)
        betterlength = len(betternums)
        found = False
        for i in range(betterlength):
            for j in range(i + 1, betterlength):
                if betternums[i] + betternums[j] == k:
                    found = True
                    break
            if found: break
        return found
