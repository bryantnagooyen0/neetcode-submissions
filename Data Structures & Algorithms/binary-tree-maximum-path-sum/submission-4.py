# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val

        def dfs(root):
            nonlocal result
            if not root:
                return 0

            maxLeft = dfs(root.left)
            maxRight = dfs(root.right)
            maxLeft = max(maxLeft, 0)
            maxRight = max(maxRight, 0)

            result = max(result, root.val + maxLeft + maxRight)

            return max(root.val + maxLeft, root.val + maxRight)

        dfs(root)
        return result
