class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #Initialize memo dict
        memo = {len(s) : True}

        #define dfs
        def dfs(i):
        #if memo[i] == true: return true
            if i in memo:
                return memo[i]
            #for w in word:
            for w in wordDict:
            #validate the len is in bounds, and check if i + w is == w
                if ((i + len(w) <= len(s)) and (s[i : i + len(w)] == w)):
            #if so move i and check if it returns true
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            #if returns true set memo and return true
            #if all words dont work return false
            memo[i] = False
            return False
        #set memo false
        return dfs(0)
