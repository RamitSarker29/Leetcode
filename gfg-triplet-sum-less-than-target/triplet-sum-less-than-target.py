class Solution:
    def countTriplets(self, sum, arr):
        #code here
        count=0
        arr.sort()
        for i in range(len(arr)-2):
            j=i+1
            k=len(arr)-1
            while (j<k):
                current_sum=arr[i]+arr[j]+arr[k]
                if current_sum<sum:
                    count+=k-j
                    j+=1
                else:
                    k-=1
        return count
