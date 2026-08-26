class Solution:
    # Function to remove all occurrences of the character from the string
    def removeCharacter(self, s, c):
        # code here
        i = 0
        j = 0
        s = list(s)
        while j < len(s) :
            if s[j] != c :
                s[i] = s[j]
                i += 1
            j += 1
        return ''.join(s[:i])

            
            
            
            
            
            
 
            
        
