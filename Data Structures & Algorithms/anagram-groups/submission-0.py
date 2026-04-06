class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            list_word = sorted(word)
            sort_word = "".join(list_word)
            if sort_word in dict:
                dict[sort_word].append(word)
            else:
                dict[sort_word] = [word]

        result = []
        for values in dict.values():
            result.append(values)
        return result

