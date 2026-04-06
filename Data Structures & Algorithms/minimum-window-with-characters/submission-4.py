class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Initialize two dictionaries
        window dict
        count dict
            populate count dict from t
        left pointer = 0
        have = 0
        need = len(t)
        res, resLen = [-1,-1] , float("infinity")
        for r in range(len(s))
            char = s[r]
            add char to window dict
            if char in count and window[char] == count[char]
                have +=
            
            while have == need:
                if (r - l + 1) < resLen
                    resLen = r - l + 1
                    res = [l,r]
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r + 1] if resLen != float("infinity") else ""

        """
        if t == "":
            return ""

        window, count = {} , {}
        l = 0
        have = 0

        for char in t:
            count[char] = 1 + count.get(char, 0)

        need = len(count)
        res, resLen= [-1,-1], float("infinity")

        

        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in count and window[char] == count[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l +=1
        l,r = res
        return s[l:r + 1] if resLen != float("infinity") else ""
