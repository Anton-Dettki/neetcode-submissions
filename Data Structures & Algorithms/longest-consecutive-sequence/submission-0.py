class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        num_set = set(nums)
        max_sequence = 0
        for num in num_set:
            if num - 1 not in num_set:
                seq = num
                sequence = 1
                while seq + 1 in num_set:
                    sequence += 1
                    seq += 1
                if sequence > max_sequence:
                    max_sequence = sequence
    
        return max_sequence
