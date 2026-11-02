class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s = sorted(nums)

        return s[len(nums)-k]