class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total = 1
        z_c = 0
        for n in nums:
            if n == 0:
                z_c += 1
            else:
                total = total * n

        ret = [0] * len(nums)

        if z_c > 1:
            return ret

        for i, v in enumerate(nums):
            if z_c:
                if v:
                    ret[i] = 0
                else:
                    ret[i] = total

            else: 
                ret[i] = int(total / v)

        return ret