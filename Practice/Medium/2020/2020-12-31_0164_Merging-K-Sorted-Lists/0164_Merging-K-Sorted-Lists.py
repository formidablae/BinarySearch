import math


class Solution:
    def solve(self, lists):
        mergedlist = []
        indexes = {}
        smallest = math.inf
        greatest = -math.inf
        for lst in lists:
            for num in lst:
                if num not in indexes.keys():
                    indexes[num] = 1
                else:
                    indexes[num] += 1
        keys = sorted(indexes.keys())
        for j in keys:
            mergedlist += [j] * indexes[j]
        # print(mergedlist)
        return mergedlist
