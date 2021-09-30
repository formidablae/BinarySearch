class Solution:
    def solve(self, lst0, lst1):
        merged_list = []
        dim0 = len(lst0)
        dim1 = len(lst1)
        mindim = min(dim0, dim1)
        i = 0
        j = 0
        while i < dim0 and j < dim1:
            if lst0[i] < lst1[j]:
                merged_list.append(lst0[i])
                i += 1
            else:
                merged_list.append(lst1[j])
                j += 1
        if j == dim1:
            merged_list = merged_list + lst0[i:dim0]
        else:
            merged_list = merged_list + lst1[j:dim1]
        return merged_list
