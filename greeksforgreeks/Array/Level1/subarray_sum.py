#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        n = len(arr)
        curr_sum = arr[0]
        start = 0
        i = 1
        while i <= n:
            while curr_sum > s and start < i-1:
                curr_sum = curr_sum - arr[start]
                start += 1
            if curr_sum == s:
                return (start+1, i)
            if i < n:
                curr_sum = curr_sum + arr[i]
            i += 1
        return (-1, '')
