#User function Template for python3

def getMinMax( a, n):
    li = []
    a = sorted(a)
    li.append(a[0])
    li.append(a[n-1])
    return li
