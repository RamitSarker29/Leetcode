class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ''
        tHashMap = {}
        sHashMap = {}
        have = 0
        required = len(set(t))
        for i in range(len(t)) :
            if t[i] in tHashMap :
                tHashMap[t[i]] += 1
            else :
                tHashMap[t[i]] = 1
        i , j = 0 , 0
        while j < len(s) :
            sHashMap[s[j]] = sHashMap.get(s[j] , 0) + 1 
            if s[j] in tHashMap and sHashMap[s[j]] == tHashMap[s[j]] :
                have += 1
            j += 1
            while have == required :
                window = s[i : j]
                if res == '' or len(res) > len(window) :
                    res = window
                if s[i] in tHashMap and sHashMap[s[i]] == tHashMap[s[i]] :
                    have -= 1
                sHashMap[s[i]] -= 1
                i += 1 
        return res
        
