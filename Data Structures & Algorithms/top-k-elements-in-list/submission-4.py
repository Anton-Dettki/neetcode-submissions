class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ret = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else: 
                freq[i] = 0
        for i in range(k):
            m = max(freq, key = freq.get)
            freq[m] = -1
            ret.append(m)

        return ret