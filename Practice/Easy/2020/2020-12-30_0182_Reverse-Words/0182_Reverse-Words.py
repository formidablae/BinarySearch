class Solution:
    def solve(self, sentence):
        return " ".join(list(map(str, sentence.split()))[::-1])
