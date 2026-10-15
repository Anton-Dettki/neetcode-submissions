class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = sum(matrix, [])

        left = 0
        right = len(nums) - 1

        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                return True
            elif nums[m] > target:
                right = m - 1
            elif nums[m] < target:
                left = m + 1
        return False