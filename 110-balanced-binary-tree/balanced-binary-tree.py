# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
                return True

        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        
        left = height(root.left)
        right = height(root.right)

        if abs(left - right) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
