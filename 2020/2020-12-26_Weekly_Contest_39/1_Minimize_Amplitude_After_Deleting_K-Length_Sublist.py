# import math
#
#
# class Solution:
#     def solve(self, nums, k):
#         self = self
#         if k == 0:
#             return max(nums) - min(nums)
#         elif len(nums) == 1 or k == len(nums) - 1 or len(nums) <= k:
#             return 0
#         else:
#             minim = math.inf
#             dim = len(nums)
#             firsthalf = []
#             secondhalf = []
#             for i in range(k - 1, len(nums)):
#                 firsthalf.clear()
#                 secondhalf.clear()
#                 if i - k + 1 > 0:
#                     firsthalf = nums[0:i - k + 1]
#                 if i + 1 < dim:
#                     secondhalf = nums[i + 1:dim]
#                 newmax = 0
#                 newmin = math.inf
#                 if len(firsthalf) > 0:
#                     newmax = max(firsthalf)
#                 if len(secondhalf) > 0:
#                     newmax = max(newmax, max(secondhalf))
#
#                 if len(firsthalf) > 0:
#                     newmin = min(firsthalf)
#                 if len(secondhalf) > 0:
#                     newmin = min(newmin, min(secondhalf))
#                 newexpr = newmax - newmin
#                 # print(firsthalf)
#                 # print(secondhalf)
#                 # print(newmax)
#                 # print(newmin)
#                 # print(minim)
#                 # print(newexpr)
#                 minim = min(minim, newexpr)
#                 # print(minim)
#             return minim
#
#
# sl = Solution()
# inp1_int_list = [1, 2, 9, 8, 7, 3]
# inp1_int = 3
# print(sl.solve(inp1_int_list, inp1_int))