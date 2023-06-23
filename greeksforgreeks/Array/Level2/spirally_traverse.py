class Solution:
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        k = 0
        l = 0
        li = []
    
        ''' k - starting row index
            m - ending row index
            l - starting column index
            n - ending column index
            i - iterator '''
    
        while (k < r and l < c):
            # Print the first row from
            # the remaining rows
            for i in range(l, c):
                li.append(matrix[k][i])
            k += 1
    
            # Print the last column from
            # the remaining columns
            for i in range(k, r):
                li.append(matrix[i][c - 1])
            c -= 1
    
            # Print the last row from
            # the remaining rows
            if (k < r):
                for i in range(c - 1, (l - 1), -1):
                    li.append(matrix[r - 1][i])
                r -= 1
    
            # Print the first column from
            # the remaining columns
            if (l < c):
                for i in range(r - 1, k - 1, -1):
                    li.append(matrix[i][l])
                l += 1
        return li
