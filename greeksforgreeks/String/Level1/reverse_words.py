class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here
        result = S.split(".")[::-1]
        return ".".join(result)
