class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
        
    def search(self, word: str) -> bool:
        idx = 0
        curr = self.root

        def dfs(idx, curr):
            if idx == len(word) and curr.isWord: return True
            if idx == len(word) or not curr.children:
                return False
            
            char = word[idx]
            if char == '.':
                for c in curr.children:
                    if dfs(idx + 1, curr.children[c]):
                        return True
                return False
            elif char in curr.children:
                return dfs(idx + 1, curr.children[char])
            else:
                return False
        
        return dfs(0, curr)
