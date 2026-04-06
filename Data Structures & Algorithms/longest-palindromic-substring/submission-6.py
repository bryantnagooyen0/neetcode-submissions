class Solution:
    def longestPalindrome(self, s: str) -> str:
        tempRes= []
        center = 1
        left = 0
        right = 2
        res = []
        if len(s) == 1:
            return s
        if len(s) == 2 and s[0] != s[1]:
            return s[0]

        #"ababd"
        while center < len(s) - 1:
            
            if left >= 0 and right < len(s) and s[left] == s[right]:
                #append string to temp res and compare to length of res
                tempRes = s[left:right + 1]
                if len(tempRes) > len(res):
                    res = tempRes
                left -= 1
                right += 1
            else:
                center += 1
                left = center - 1
                right = center + 1
        
        #"abbc"
        left = 0
        right = 1
        center = 1
        # check if left and right equal to eachother
        # if they are then add it to temp res, check against res and increment both pointers
        #if they arent then move both pointers
        while center < len(s):
            left = center - 1
            right = center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left:right + 1]) > len(res):
                    res = s[left:right + 1]
                left -= 1
                right += 1
            else:
                center += 1




        return res




       

        