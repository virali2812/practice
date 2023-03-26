# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        if(len(arr) == 1):
            return 0
        for i in range(len(arr)):
            if(i != len(arr) - 1 and arr[i] > arr[i + 1]):
                return i
            elif(i == len(arr) - 1 and arr[i] > arr[i - 1]):
                return i
            #print(arr[i])
        return 1

