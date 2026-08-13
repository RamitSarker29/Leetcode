class Solution:
    def nextLargerElement(self, arr):
        # code here
        stack = []
        res =[-1]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            while len(stack) !=0 and stack[-1] <= arr[i]:
                stack.pop()
            if len(stack) !=0 and stack[-1] > arr[i]:
                res[i] = stack[-1]
            stack.append(arr[i])
        return res
