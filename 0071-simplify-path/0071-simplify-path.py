class Solution:
    def simplifyPath(self, path: str) -> str:
        pathStack = []
        currFileOrDir = []
        path = list(path)
        if path[-1] != '/':
            path.append('/')
        for l in path:
            if l == '/':
                if len(currFileOrDir) > 0:
                    pathStack.append("".join(currFileOrDir))
                currFileOrDir = []
            else:
                currFileOrDir.append(l)
            if pathStack and pathStack[-1] == "..":
                pathStack.pop()
                if pathStack:
                    pathStack.pop()
            if pathStack and pathStack[-1] == ".":
                pathStack.pop()

        absPath ="/" + "/".join(pathStack)
        return absPath 




