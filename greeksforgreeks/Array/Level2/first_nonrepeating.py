#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr, n): 
        # Complete the function
        # Create an empty dictionary to keep track of element counts
        count_dict = {}
        
        # Loop through the array and increment the count for each element
        for i in range(n):
            if arr[i] in count_dict:
                count_dict[arr[i]] += 1
            else:
                count_dict[arr[i]] = 1
        
        # Loop through the array again and return the index of the first element with a count of 1
        for i in range(n):
            if count_dict[arr[i]] == 1:
                return arr[i]
        
        # If no non-repeating element is found, return -1
        return -1

