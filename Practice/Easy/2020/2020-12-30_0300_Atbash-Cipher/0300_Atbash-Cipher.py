class Solution:
    def solve(self, text):
        result = ""
        for i in range(len(text)):
            result += chr(219 - ord(text[i]))
        return result
