"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
import collections
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node is None:
            return None

        correspondency = {}
        return self.DFS(node, correspondency)

    def DFS(self, currNode, correspondency):
        currCopy = None
        if currNode.val in correspondency:
            return correspondency[currNode.val]
        else:
            currCopy = correspondency[currNode.val] = Node(currNode.val)

        for n in currNode.neighbors:
            neighborCopy = self.DFS(n,correspondency)
            currCopy.neighbors.append(neighborCopy)
        return currCopy



        



