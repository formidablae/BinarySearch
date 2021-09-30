class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        arrset = set(arr)
        count = 0
        for lst in pieces:
            lastindex = -1
            newcount = 0
            for j in range(len(lst)):
                # print("j", j, "count", count, "newcount", newcount, "lst[]", lst[j])
                if lst[j] in arrset:
                    newindex = arr.index(lst[j])
                    # print("lastindex", lastindex, "newindex", newindex)
                    if lastindex == -1 or newindex == lastindex + 1:
                        newcount += 1
                        lastindex = newindex

                    else:
                        break
                else:
                    break
            # print("count", count, "newcount", newcount)
            count += newcount
        return count == len(arr)
