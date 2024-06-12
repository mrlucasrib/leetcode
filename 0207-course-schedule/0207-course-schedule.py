class Solution:
    stack = []
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visitedPath = {}
        adjList = self.makeAdjList(numCourses-1, prerequisites)
        for course in range(numCourses):
            if course in adjList and course not in visitedPath:
                if self.hasCycleDFS(course, visitedPath, adjList):
                    return False
        return True

    def hasCycleDFS(self, currNode, visitedPath, adjList):
        if visitedPath.get(currNode, False):
            return True
        if currNode in visitedPath:
            return False
        visitedPath[currNode] = True

        for node in adjList[currNode]:
            hasCycle = self.hasCycleDFS(node, visitedPath, adjList)
            if hasCycle:
                return True

        visitedPath[currNode] = False
        return False

    def makeAdjList(self, numCourses, prerequisites):
        adjList = {}
        for req in prerequisites:
            if req[0] in adjList:
                adjList[req[0]].append(req[1])
            else:
                adjList[req[0]] = [req[1]]
            if req[1] not in adjList:
                adjList[req[1]] = []
        return adjList