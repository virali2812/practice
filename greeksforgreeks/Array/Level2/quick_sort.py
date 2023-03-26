#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = Solution.partition(self,arr, low, high)
     
            # Recursive call on the left of pivot
            Solution.quickSort(self, arr, low, pi - 1)
     
            # Recursive call on the right of pivot
            Solution.quickSort(self, arr, pi + 1, high)
    
    def partition(self,arr,low,high):
        # code here
        # choose the rightmost element as pivot
        pivot = arr[high]
 
        # pointer for greater element
        i = low - 1
     
        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if arr[j] <= pivot:
     
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1
     
                # Swapping element at i with element at j
                (arr[i], arr[j]) = (arr[j], arr[i])
     
        # Swap the pivot element with the greater element specified by i
        (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
     
        # Return the position from where partition is done
        return i + 1
    
