from collections import deque
class Solution:
    def _makeAdjList(self, n, edges):
        adjList = defaultdict(list)
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        return adjList

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adjList = self._makeAdjList(n, edges)

        leaves = deque()
        nodeRanks = defaultdict(list)
        for src, neighbors in adjList.items():
            nodeRanks[src] = len(neighbors)
            if len(neighbors) == 1:
                leaves.append(src)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for neig in adjList[node]:
                    nodeRanks[neig] -= 1
                    if nodeRanks[neig] == 1:
                        leaves.append(neig)
                 
        