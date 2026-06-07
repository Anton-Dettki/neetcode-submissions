class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) - 1
        i = 0
        while(True):
            start = numbers[i]
            end = numbers[n]

            if start + end == target:
                return [i+1, n+1]
            if start + end > target:
                n -= 1
                end = numbers[n]
            if start + end < target:
                i += 1
                start = numbers[i]
