import pdb
import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def diffByOne(y,z):
	   count = 0
	   for c1, c2 in zip(y,z):
	      if (c1 != c2):
		  count +=1 
		  if count > 1: break
	   return count == 1 

        class Node(object):
           def __init__(self, val):
	       self.val = val
	       self.visited = []
	       self.nextNodes = []

        origin = Node(beginWord)
        origin.vistied = [origin]
        allNodes = [origin]
        endNode = None
        for word in wordList:
           nnode = Node(word)
           if word == endWord:
 	      endNode = nnode
 	   for node in allNodes:
 	      if (diffByOne(nnode.val, node.val)):
 	         nnode.nextNodes.append(node)
 	         node.nextNodes.append(nnode)
           
 	   allNodes.append(nnode)
    
        finalPath = []
        toTraverse = [origin]

        while toTraverse:
           node = toTraverse.pop(0)
           for nextNode in node.nextNodes:
              if (not nextNode.visited or len(nextNode.visited) > len(nextNode.visited) +1): 
                 # found a shorter path 
                 nextNode.visited = node.visited + [nextNode]
                 toTraverse.append(nextNode)
        if (endNode and endNode.visited):
           print [ n.val  for n in endNode.visited]
	   return len(endNode.visited) +1
        return 0

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# print(Solution().ladderLength( beginWord, endWord, wordList))
# wordList = ["hot","dot","dog","lot","log"]
# print(Solution().ladderLength( beginWord, endWord, wordList))
# beginWord = "hot"
# endWord = "dog"
# wordList = ["hot","dog"]
# print(Solution().ladderLength( beginWord, endWord, wordList))
# 

beginWord = "nape"
endWord = "mild"
