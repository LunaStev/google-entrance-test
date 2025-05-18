class Solution:
    def romanToInt(self, s: str) -> int:
        rm = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and rm[s[i]] < rm[s[i + 1]]:
                result += rm[s[i + 1]] - rm[s[i]]
                i += 2
            else:
                result += rm[s[i]]
                i += 1

        return result
        
