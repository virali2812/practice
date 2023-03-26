#User function Template for python3

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        return sorted(list(set(A).intersection(B, C)))
