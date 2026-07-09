class TrieNode:
    def __init__(self, isWord=False):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.trie

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.isWord = True
                 
    def search(self, word: str) -> bool:
        curr = self.trie

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.isWord

        # fail conditions: if curr reaches end and not isWord OR curr doesn't reach end of search

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True
        
        