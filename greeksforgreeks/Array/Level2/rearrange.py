#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        p_li = [i for i in arr if i >= 0]
        n_li = [i for i in arr if i < 0]
        for i,c in enumerate(p_li):
            n_li.insert(i*2,c)
        arr[:] = n_li[:]
        # print(arr)
        # return arr
