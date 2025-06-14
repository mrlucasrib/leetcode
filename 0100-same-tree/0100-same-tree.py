from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = deque([p])
        q_queue = deque([q])

        while p_queue and q_queue:
            p_node = p_queue.popleft()
            q_node = q_queue.popleft()

            if bool(p_node) != bool(q_node):
                return False 
            elif (p_node and q_node and
                p_node.val != q_node.val):
                return False
            if p_node:
                p_queue.append(p_node.left)
                p_queue.append(p_node.right)
            if q_node:
                q_queue.append(q_node.left)
                q_queue.append(q_node.right)
        return True
