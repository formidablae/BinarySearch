class Solution:
    def solve(self, s):
        counter = 1
        answer = ""
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                counter += 1
            else:
                answer += str(counter) + s[i - 1]
                counter = 1
        answer += str(counter) + s[len(s) - 1]
        return answer
