class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) :
            return False
        s1Array = [0] * 26
        s2Array = [0] * 26
        for i in range(len(s1)) :
            index = ord(s1[i]) - ord('a')
            s1Array[index] += 1
        for i in range(len(s1)) :
            index = ord(s2[i]) - ord('a')
            s2Array[index] += 1
            if s1Array == s2Array :
                return True
        i = 0
        j = len(s1)
        while j < len(s2) :
            index = ord(s2[i]) - ord('a')
            s2Array[index] -= 1
            index = ord(s2[j]) - ord('a')
            s2Array[index] += 1
            if s1Array == s2Array :
                return True
            i += 1
            j += 1
        return False 
        