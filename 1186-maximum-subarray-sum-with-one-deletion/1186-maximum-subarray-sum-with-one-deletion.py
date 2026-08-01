class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_deleted=arr[0]
        one_deleted=0
        ans=arr[0]
        for i in range(1,len(arr)):
            prev_one_deleted=one_deleted
            prev_no_deleted=no_deleted
            no_deleted=max(prev_no_deleted+arr[i],arr[i])
            one_deleted=max(prev_one_deleted+arr[i],prev_no_deleted)
            ans=max(ans,no_deleted,one_deleted)
        return ans


        