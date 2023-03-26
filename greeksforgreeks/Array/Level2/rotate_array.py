#User function Template for python3

def rotate( arr, n):
    li = arr.copy()
    for i in range(1, n):
        arr[i] = li[i-1]
    arr[0] = li[n-1]
