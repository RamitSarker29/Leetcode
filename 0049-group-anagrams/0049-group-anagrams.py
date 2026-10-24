class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for i in range(len(strs)) :        
            hash_map = [0] * 26
            for j in range(len(strs[i])) :
                char = strs[i][j]
                hash_map[ord(char) - ord('a')] += 1
            key = tuple(hash_map)
            if key not in groups :
                groups[key] = []
            groups[key].append(strs[i])
        return list(groups.values())
        


        