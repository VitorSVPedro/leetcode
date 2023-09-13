class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        rslt, A, B = 0, 0, 0

        while A < len(s) and B < len(s):
            if s[B] not in chars:
                chars.add(s[B])
                B += 1
                if len(chars) > rslt:
                    rslt = len(chars)
            else:
                A += 1
                chars.clear()
                B = A
            
        return rslt