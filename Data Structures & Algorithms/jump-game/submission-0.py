class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if farthest < i:
                return False

            if farthest >= len(nums) - 1:
                return True
            
            farthest = max(farthest, i + nums[i])


        return farthest >= len(nums) - 1