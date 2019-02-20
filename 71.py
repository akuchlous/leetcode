class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if (path == "/"): return path 
        if (path == "/../"): return "/"
        steps = path.split("/")
        newP = []
        for s in steps:
            if ((s == ".") or (s == "")): 
                continue
            elif (s == ".." and len(newP)>=1):
                del newP[-1]
            else:
                newP.append(s)
        return  "/"+"/".join(newP)


print(Solution().simplifyPath("/home/"))
print(Solution().simplifyPath("/home"))
print(Solution().simplifyPath("/a//b////c/d//././/.."))
print(Solution().simplifyPath("/../"))
