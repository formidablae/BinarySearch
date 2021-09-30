class Solution:
    def solve(self, num):
        if num == 0:
            return 0
        else:
            summat = 0
            while num >= 10:
                summat += num % 10
                num = (num - (num % 10)) // 10
            summat += num
            return summat
