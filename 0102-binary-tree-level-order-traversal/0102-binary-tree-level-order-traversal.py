from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(0,root)])
        last_level = 0
        ans = [[]]
        if root is None:
            return []
        while queue:
            level, node = queue.popleft()
            if last_level == level:
                ans[-1].append(node.val)
            else:
                last_level = level
                ans.append([node.val])
            if node.left is not None:
                queue.append((level+1,node.left))
            if node.right is not None:
                queue.append((level+1,node.right))
        return ans


