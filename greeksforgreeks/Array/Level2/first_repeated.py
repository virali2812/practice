#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        
        #arr : given array
        #n : size of the array
        unique_set = set(arr)
        if(len(unique_set) == len(arr)):
            return -1
        else:
            for i in range(len(arr)):
                if arr[i] in arr[i+1: len(arr)]:
                    return i + 1
