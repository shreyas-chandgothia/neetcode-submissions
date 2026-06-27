class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_diff = dict()
        for i in range(len(s)):
            freq_diff[s[i]] = freq_diff.get(s[i],0) + 1
            freq_diff[t[i]] = freq_diff.get(t[i],0) - 1
        for val in freq_diff.values():
            if val != 0:
                return False
        return True
