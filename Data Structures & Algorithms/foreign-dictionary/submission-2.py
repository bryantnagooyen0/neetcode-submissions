class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #get the words from the list
        adj = {c : set() for w in words for c in w}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            #once we have words, iterate through letters of both till we find differing character
            minlen = min(len(word1), len(word2))
            #check if later word is same prefix but shorter, if so return ""
            if word2[:minlen] == word1[:minlen] and len(word1) > len(word2):
                return ""
            #put differing character into adj hashmap with word_1 letter as key
            for i in range(minlen):
                if word1[i] != word2[i]:
                    adj[word1[i]].add(word2[i])
                    break

        #initialize visited hashmap
        visited = {}
        #define DFS function
        result = []
        def dfs(char):
        # if char in visited return visited[char]
            if char in visited:
                return visited[char]
        #set char to true in visited hashmap
            visited[char] = True
        #loop through neighborcharacters and dfs through
            for neighChar in adj[char]:
                #if dfs returns true then return true
                if dfs(neighChar):
                    return True
        #set char to false
            visited[char] = False
        # add to result
            result.append(char)

        #for char in adj, dfs through
        for char in adj:
            if dfs(char):
                return ""
        #if dfs returns true, return ""

        #reverse result list and return result
        result.reverse()
        return "".join(result)
        
