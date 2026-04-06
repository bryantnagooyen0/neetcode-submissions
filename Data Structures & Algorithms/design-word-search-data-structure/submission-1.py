class TrieNode:
    def __init__(self):
        self.children ={}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        

        def dfs(i, root):
            if i == len(word):
                return root.isEnd
            char = word[i]
            if char == ".":
                for node in root.children.values():
                    if dfs(i + 1, node):
                        return True
                return False
            #If its a regular character
            if char not in root.children:
                return False
            return dfs(i + 1, root.children[char])
        
        return dfs(0,self.root)

            



        
