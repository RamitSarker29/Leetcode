class Solution:
    def removeConsecutiveSame(self, arr):
        # code here
        stack = []
        for i in range(len(arr)):
            if len(stack)!=0:
                if stack[-1] == arr[i]: 
                    stack.pop()
                else:
                    stack.append(arr[i])
            else:
                stack.append(arr[i])

        return len(stack)

