class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resIdx = 0
        resLength = 0

        for i in range(len(s)):
            
            r, l = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLength:
                    resLength = r - l + 1
                    resIdx = l
                r += 1
                l -= 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLength:
                    resLength = r - l + 1
                    resIdx = l
                r += 1
                l -= 1

        return s[resIdx : resIdx + resLength]

            

        