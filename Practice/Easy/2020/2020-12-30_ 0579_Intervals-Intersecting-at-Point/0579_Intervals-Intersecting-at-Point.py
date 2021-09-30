class Solution:
    def solve(self, intervals, point):
        count = 0
        for interval in intervals:
            if interval[0] <= point and interval[1] >= point:
                count += 1
        return count
