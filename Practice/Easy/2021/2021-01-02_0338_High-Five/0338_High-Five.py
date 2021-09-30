class Solution:
    def solve(self, n):
        st_n = str(n)
        flag = False
        if n >= 0:
            n_list = [int(x) for x in st_n]
            for i in range(len(n_list)):
                if n_list[i] < 5:
                    n_list.insert(i, 5)
                    flag = True
                    break
            if not flag:
                n_list.append(5)
            return int("".join(map(str, n_list)))
        else:
            n_list = [int(x) for x in st_n[1:]]
            for i in range(len(n_list)):
                if n_list[i] > 5:
                    n_list.insert(i, 5)
                    flag = True
                    break
            if not flag:
                n_list.append(5)
            return int("-" + "".join(map(str, n_list)))


sl = Solution()
inp1 = 923
inp2 = -234
inp3 = 1
print(sl.solve(inp1))
print(sl.solve(inp2))
print(sl.solve(inp3))