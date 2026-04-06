class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.index = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Insert all the words into a trie, make sure end node is marked as end and have
         end node save the index of the word in words list

         
        Traverse and backtrack method:
        get row and col  from parameters
        if board[row][col] in cur.children:
            cur = cur.children[board[row][col]]
            move to different cell, and check if that letter is in cur.children




        """
        root = TrieNode()

        for i in range(len(words)):
            cur = root
            word = words[i]
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.isEnd = True
            cur.index = i
        
        cur = root
        def dfs(row,col, cur,result):
            
            
            #if character is in boundaries,and in cur.children, and not #
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] == "#" or board[row][col] not in cur.children:
                return None
            
            c = board[row][col]

            #change node to next node
            cur = cur.children[c]

            #if node is end node, append word
            if cur.isEnd == True:
                result.append(words[cur.index])
                cur.isEnd = False
                
            board[row][col] = "#"
            (dfs(row + 1, col, cur, result) or dfs(row - 1,col, cur, result) or dfs(row,col + 1, cur, result) or dfs(row,col - 1, cur, result))
            
            #revert # back to letter
            board[row][col] = c

        result = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row,col,root,result)
        return result


        