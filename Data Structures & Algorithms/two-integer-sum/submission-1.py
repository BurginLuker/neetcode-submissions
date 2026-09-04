class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i in range(len(nums)):
            needs = target - nums[i]
            if needs in m:
                return [m[needs], i]
            m[nums[i]] = i
