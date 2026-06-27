class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def freqTuple(word):
            out = [0]*26
            for character in word:
                out[ord(character)-ord('a')] += 1
            return tuple(out)
        anagrams = dict()
        for word in strs:
            word_key = freqTuple(word)
            anagrams[word_key] = anagrams.get(word_key, []) + [word] 
        return list(anagrams.values())