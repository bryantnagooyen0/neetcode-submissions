class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            delimiter_pos = s.find("#", i)

            length = int(s[i:delimiter_pos])

            start_pos = delimiter_pos + 1
            actual_string = s[start_pos:start_pos + length]
            result.append(actual_string)

            i = start_pos + length
        return result
