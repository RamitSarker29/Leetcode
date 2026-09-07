# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root.right
        def fun (p , q) :
            if p == None and q == None :
                return True
            if p == None or q == None :
                return False
            if p.val != q.val :
                return False
            if not fun (p.left , q.right) :
                return False
            if not fun (p.right , q.left):
                return False
            return True
        return fun (p , q)
        