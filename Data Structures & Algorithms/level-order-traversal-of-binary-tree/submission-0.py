# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        create a queue
        add the root to the queue
        while there is a queue:
            initialize level
            len of queue
            for length of queue:
                if node
                pop first node
                add node to level
                add children to queue
            if level:
                append level to result

        """

        q = collections.deque()
        q.append(root)
        result = []


        while q:
            level = []
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)
        return result



