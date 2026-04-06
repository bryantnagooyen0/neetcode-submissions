class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #initialize hashmap
        adj = {c : set() for w in words for c in w}
        #get word1 and word2
        result = []

        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i + 1]
            min_len = min(len(word_1), len(word_2))
            if word_1[:min_len] == word_2[:min_len] and len(word_2) < len(word_1):
                return ""
            
            for c in range(min_len):
                if word_1[c] != word_2[c]:
                    adj[word_1[c]].add(word_2[c])
                    break
                
        #define dfs function
        visited = {}
        def dfs(char):
            
            if char in visited:
                return visited[char]

            visited[char] = True
            
            #dfs through neighbors until we reach the last character
            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True
            # add character to result 
            visited[char] = False
            result.append(char)
            
        #run dfs and if it returns true then return ""
        for char in adj.keys():
            if dfs(char):
                return ""
        #reverse result and return
        result.reverse()
        return "".join(result)
