class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        parent = self.root
        buf = ""
        for c in word:
            buf+=c
            if (buf not in parent):
                parent[buf] = {}
            parent = parent[buf]
        # handle cases like 
        # ten, tent 
        parent[" "] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        buf = ""
        parent = self.root
        for c in word:
            buf+=c
            if buf not in parent : return False 
            parent = parent[buf]
        return " " in parent  

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        parent  = self.root
        buf = ""
        for c in prefix:
            buf+=c
            if buf not in parent : return False 
            parent = parent[buf]
        return True
        
