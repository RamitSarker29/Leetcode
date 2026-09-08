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
            if root.val > p.val and root.val > q.val:
                return fun (root.left)
            if  root.val < p.val and root.val < q.val :
                return fun (root.right)
            return root
        return fun (root)