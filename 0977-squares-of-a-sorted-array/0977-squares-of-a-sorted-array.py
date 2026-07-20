class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        res=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        for i in range(len(neg)):
            neg[i]=neg[i]*neg[i]
        for i in range(len(pos)):
            pos[i]=pos[i]*pos[i]
        neg=neg[::-1]
        i=0
        j=0
        while (i<len(neg) and j<len(pos)):
            if neg[i]<pos[j]:
                res.append(neg[i])
                i+=1
            else:
                res.append(pos[j])
                j+=1
        while (j<len(pos)):
            res.append(pos[j])
            j+=1
        while (i<len(neg)):
            res.append(neg[i])
            i+=1
        return res
        