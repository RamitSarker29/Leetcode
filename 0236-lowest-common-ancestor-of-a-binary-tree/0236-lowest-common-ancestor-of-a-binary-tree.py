# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def fun (root) :
            if root == None :
                return None
            if p == root or q == root :
                return root
            left = fun (root.left)
            right = fun (root.right)
            if left != None and right != None :
                return root
            if left != None :
                return left
            if right != None :
                return right
        return fun (root)