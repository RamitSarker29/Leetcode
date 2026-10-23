class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        hash_map ={}
        for i in range(len(s)) :
            if s[i] in hash_map :
                hash_map[s[i]] += 1
            else :
                hash_map[s[i]] = 1
        for i in range(len(t)) :
            if t[i] in hash_map :
                hash_map[t[i]] -= 1
                if hash_map[t[i]] == 0:
                    del hash_map[t[i]]
            else :
                return False
        if len(hash_map) == 0 :
            return True 