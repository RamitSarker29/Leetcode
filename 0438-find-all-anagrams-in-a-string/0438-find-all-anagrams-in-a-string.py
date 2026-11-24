class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p) :
            return []
        pHashMap = {}
        sHashMap = {}
        res= []
        for i in p :
            if i in pHashMap :
                pHashMap[i] += 1
            else :
                pHashMap[i] = 1
        for i in range(len(p)) :
            if s[i] in sHashMap :
                sHashMap[s[i]] += 1
            else  :
                sHashMap[s[i]] = 1
        if sHashMap == pHashMap :
            res.append(0)
        i = 0
        j = len(p)
        while j < len(s) :
            if s[j] in sHashMap :
                sHashMap[s[j]] += 1
            else :
                sHashMap[s[j]] = 1
            j += 1
            sHashMap[s[i]] -= 1
            if sHashMap[s[i]] == 0 :
                del sHashMap[s[i]]
            i += 1
            if sHashMap == pHashMap :
                res.append(i)
        return res
        
