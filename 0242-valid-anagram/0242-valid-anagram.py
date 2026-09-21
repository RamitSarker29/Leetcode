class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        for i in s :
            if i in hash_map :
                hash_map[i] += 1
            else :
                hash_map[i] = 1
        for j in t :
            if j in hash_map :
                hash_map[j] -= 1
                if hash_map[j] == 0 :
                    del hash_map[j]
            else :
                return False
        return False if len(hash_map) > 0 else True
                    
            

        
        
        