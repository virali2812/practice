from collections import Counter
class Solution:
    def duplicates(self, arr, n): 
        # code here
        d = Counter(arr)
        duplicateList = list([item for item in d if d[item]>1])
        if(len(duplicateList) == 0):
            duplicateList.append(-1)
        return sorted(duplicateList)
            
