class Solution:
    def solve(self, n):
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0 or "3" in list(str(i)) or "6" in list(str(i)) or "9" in list(str(i)):
                ans.append("clap")
            else: ans.append(str(i))
        return ans
