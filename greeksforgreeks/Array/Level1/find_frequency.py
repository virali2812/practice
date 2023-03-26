#User function Template for python3

"""
You're given an array (arr) of length n
Return the frequency of element x in the given array
"""
def findFrequency (arr, n, x):
    # Your Code Here
    res = 0
    for i in range(len(arr)):
        if(arr[i] == x):
            res += 1
    return res
