class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        if len(s) < 26:
            return 0
        else:
            char_set = set()
            for ch in s:
                # If the character is already
                # a lowercase character
                if ch >= 'a' and ch <= 'z':
                    char_set.add(ch)
                    
                # In case of a uppercase character
                if ch >= 'A' and ch <= 'Z':
                    # convert to lowercase
                    ch = ch.lower()
                    char_set.add(ch)
 
        # check if the size is 26 or not
        return 1 if len(char_set) == 26 else 0
