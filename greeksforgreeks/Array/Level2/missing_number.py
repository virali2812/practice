#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        # code here
        n = len(array)
        total = (n + 1)*(n + 2)/2
        arr_sum = sum(array)
        return int(total - arr_sum)
