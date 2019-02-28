"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = set()
        toProcessNodes = [node]
        mapping  = {}
        retVal = None
        while (toProcessNodes):
            n = toProcessNodes.pop(0)
            if (n not in visited):
                visited.add(n)
                newNode = Node(n.val, n.neighbors)
                mapping[n] = newNode
                if (retVal == None): 
                    retVal = newNode
                
                toProcessNodes.extend(n.neighbors)
                
                
        for _, newNode in mapping.iteritems(): 
            newList = []
            neighbors = newNode.neighbors 
            for n in neighbors:
                if n in mapping :
                    newList.append(mapping[n])
                else :
                    newList.append(n)
            newNode.neighbors = newList
            
        return retVal
    
