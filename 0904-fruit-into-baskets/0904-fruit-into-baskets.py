class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i,j=0,0
        max_fruit=0
        hash_map={}
        for j in range (len(fruits)):
            if fruits[j] in hash_map:
                hash_map[fruits[j]]+=1
            else:
                hash_map[fruits[j]]=1
            while len(hash_map)>2:
                hash_map[fruits[i]]-=1
                if hash_map[fruits[i]]==0:
                    del hash_map[fruits[i]]
                i+=1
            max_fruit=max(max_fruit,j-i+1)
        return max_fruit