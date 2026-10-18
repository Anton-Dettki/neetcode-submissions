class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}

        for i in range(0,len(nums)):
            complement = target - nums[i]

            if complement in hashSet:
                return [hashSet[complement], i]
            else:
                hashSet[nums[i]] = i