class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers)):
            for j in range(0, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    if i < j:
                        return [i+1, j+1]
                    else:
                        return [j+1, i+1]
                    