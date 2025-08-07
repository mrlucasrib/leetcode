from collections import defaultdict, Counter, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        node_degree = {node: 0 for node in range(numCourses)}
        ans = []
        for k, v in prerequisites:
            adj_list[k].append(v)
            node_degree[v] += 1

        queue_nodes = deque()
        for node, degree in sorted(node_degree.items(), key=lambda x: x[1]):
            if degree == 0:
                queue_nodes.append(node)

        while queue_nodes:
            node = queue_nodes.popleft()
            ans.append(node)
            for neighbor in adj_list[node]:
                node_degree[neighbor] -= 1
                if node_degree[neighbor] == 0:
                    queue_nodes.append(neighbor)
            
        if len(ans) < numCourses:
            return []
        return list(reversed(ans))
            
