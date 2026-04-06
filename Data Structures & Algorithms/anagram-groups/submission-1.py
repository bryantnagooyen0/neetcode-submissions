class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        
        """
        sort first word, have first word sorted as key and non-sorted word as value
        check if second word sorted fits in first sorted word, if not create another key

        """
        anaDict = {}

        for word in strs:
            sort_word = "".join(sorted(word))

            if sort_word in anaDict:
                anaDict[sort_word].append(word)
            else:
                anaDict[sort_word] = [word]
        
        values = anaDict.values()
        result = list(values)
        return result

