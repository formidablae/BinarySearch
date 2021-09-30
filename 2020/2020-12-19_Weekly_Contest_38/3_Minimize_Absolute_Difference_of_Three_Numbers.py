# import math
#
#
# def solve(a, b, c):
#     minim = math.inf
#     for i in range(len(a)):
#         for j in range(len(b)):
#             for k in range(len(c)):
#                 minim = min(minim, abs(a[i] - b[j]) + abs(b[j] - c[k]))
#     return minim
#
#
# a_list = [1, 8, 5]
# b_list = [2, 9]
# c_list = [5, 4]
# print(solve(a_list, b_list, c_list))