# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def fun (root) :
            if root == None :
                return None
            left = root.left
            right = root.right
            if val > root.val :
                return fun (right)
            if val < root.val :
                return fun (left)
            else :
                return root
        return fun (root)
        