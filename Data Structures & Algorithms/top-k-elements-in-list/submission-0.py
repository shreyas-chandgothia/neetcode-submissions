class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        reverseFreq = []
        for key, val in freq.items():
            reverseFreq.append([val, key])
        reverseFreqSorted = sorted(reverseFreq, reverse=True)
        output = []
        for i in range(k):
            output.append(reverseFreqSorted[i][1])
        return output