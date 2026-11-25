class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p) :
            return []
        pHashMap = [0] * 26
        sHashMap = [0] * 26
        res = []
        for i in range(len(p)) :
            index = ord(p[i]) - ord('a')
            pHashMap[index] += 1
        for i in range(len(p)) :
            index = ord(s[i]) - ord('a')
            sHashMap[index] += 1
        if sHashMap == pHashMap :
            res.append(0)
        i = 0
        j = len(p)
        while j < len(s) :
            index = ord(s[i]) - ord('a')
            sHashMap[index] -= 1
            index = ord(s[j]) - ord('a')
            sHashMap[index] += 1
            if sHashMap == pHashMap :
                res.append(i + 1)
            i += 1
            j += 1
        return res


        