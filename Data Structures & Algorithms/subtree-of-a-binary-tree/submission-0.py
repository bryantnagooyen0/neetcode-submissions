# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Have a helper function that checks if its the same tree
        First check if root and subroot are same tree
        if not we go down left and check if left is same tree as subroot
        go down right and check if right is same tree as subroot
        """

        if self.sameTree(root, subRoot) is True:
            return True
            
        if not root:
            return False
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        

    def sameTree(self, tree1, tree2):
        if not tree1 and not tree2:
            return True

        if not tree1 or not tree2 or tree1.val != tree2.val:
            return False
        
        return self.sameTree(tree1.left, tree2.left) and self.sameTree(tree1.right, tree2.right)


