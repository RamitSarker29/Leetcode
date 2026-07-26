class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        i=0
        j=k-1
        sum1=0
        max_sum=0
        window_sum=sum(arr[0:k])
        max_sum=window_sum
        while (j<len(arr)-1):
            window_sum=window_sum-arr[i]+arr[j+1]
            max_sum=max(window_sum,max_sum)
            i+=1
            j+=1
        return max_sum
            
