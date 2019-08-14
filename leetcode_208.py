"""Trie, also called prefix tree"""
class Node:
    def __init__(self, val):
        self.val = val
        self.isWord = False
        self.child = {}


class Trie:

    def __init__(self):
        """
        has a node structure, and a root
        
        """
        self.root = Node("")
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node.child:
                #append the children
                node.child[char] = Node(char)
            #descend node to node.child that has the previous char, simlar to node = node.left
            node = node.child.get(char)
        node.isWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        #start from the root
        node = self.root
        for char in word:
            if char in node.child:
                node = node.child.get(char)
            else:
                return False
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char in node.child:
                node = node.child.get(char)
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)