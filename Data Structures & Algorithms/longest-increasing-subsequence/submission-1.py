class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def findPath(i):
            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]

            m = 1

            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    m = max(m, 1 + findPath(j))
            
            cache[i] = m
            return m
            


        m = 0
        for i in range(len(nums)):
            m = max(findPath(i), m)

        return m