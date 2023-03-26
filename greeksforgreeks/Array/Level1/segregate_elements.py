#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        temp1 = []
        temp2 = []
        for i in range(n):
            if(arr[i] > 0):
                temp1.append(arr[i])
            elif(arr[i] < 0):
                temp2.append(arr[i])
        
        j = 0
        for i in temp1+temp2:
            arr[j] = i
            j += 1
                
