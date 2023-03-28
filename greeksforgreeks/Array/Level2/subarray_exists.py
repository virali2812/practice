#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        if 0 in arr:
            return True
        else:
            n_sum = 0
            s = set()
            for i in range(n):
                n_sum += arr[i]
                if n_sum == 0 or n_sum in s:
                    return True
                s.add(n_sum)
        return False
