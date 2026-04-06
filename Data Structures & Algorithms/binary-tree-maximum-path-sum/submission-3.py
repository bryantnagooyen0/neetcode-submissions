# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        result = root.val
        helper dfs function
        base case
        get max of left tree
        get max of right tree
        make sure max isnt negative for both
        check if node as the switching point is higher than result, result = max(result, root.val + left + right)

        return max(left + root.val, right + root.val)

        """

        result = root.val

        def dfs(root):
            nonlocal result
            if not root:
                return 0
            
            maxLeft = dfs(root.left)
            maxRight = dfs(root.right)
            maxLeft = max(maxLeft, 0)
            maxRight= max(maxRight, 0)

            #result = max(result, root.val + maxLeft, root.val + maxRight)

            result = max(result, root.val + maxLeft + maxRight)

            return max(maxLeft + root.val, maxRight + root.val)
        
        dfs(root)
        return result




