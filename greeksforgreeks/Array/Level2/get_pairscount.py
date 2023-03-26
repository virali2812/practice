#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        unordered_map = {}
        count = 0
        for i in range(n):
            if (k - arr[i]) in unordered_map:
                count += unordered_map[k - arr[i]]
            if arr[i] in unordered_map:
                unordered_map[arr[i]] += 1
            else:
                unordered_map[arr[i]] = 1
        return count
