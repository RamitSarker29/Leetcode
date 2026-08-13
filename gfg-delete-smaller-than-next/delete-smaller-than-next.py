class Solution:
    def deleteElement(self,arr,k):
        # Code here
        stack =[]
        for i in range(len(arr)):
            while len(stack) !=0 and stack[-1] < arr[i] and k!=0:
                stack.pop()
                k-=1
            stack.append(arr[i])
        return stack
            
