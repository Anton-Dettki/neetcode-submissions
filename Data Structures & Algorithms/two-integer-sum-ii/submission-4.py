class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            currSum = numbers[left] + numbers[right]

            if target == currSum:
                return [left+1, right+1]

            elif target >= currSum:
                left += 1
            elif target <= currSum:
                right -= 1


        # 1,4,6,8   t=10    ret=[int, int]

        #l=0     r=3     1+8=9
        #l=1     r=3     4+8=12
        #l=1     r=2     4+6=10
        #return [l+1, r+1]
