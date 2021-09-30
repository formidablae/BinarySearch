class Solution:
    def solve(self, num):
        digits = []
        while True:
            digit = num % 10
            digits.append(digit)
            if num - digit == 0: break
            else: num = ((num - digit) / 10)
        length = len(digits)
        for i in range(int(length / 2)):
            if digits[i] != digits[length - i - 1]: return False
        return True
