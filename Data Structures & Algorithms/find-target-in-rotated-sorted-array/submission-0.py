
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            m = (left + right) // 2

            if nums[m] == target:
                return m

            elif nums[m] < nums[right]:  # Right half is sorted
                if nums[m] < target <= nums[right]:
                    left = m + 1
                else:
                    right = m - 1

            else:  # Left half is sorted
                if nums[left] <= target < nums[m]:
                    right = m - 1
                else:
                    left = m + 1

        return -1
