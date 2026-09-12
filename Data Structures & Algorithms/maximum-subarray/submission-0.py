class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = float('-inf')
        prefix = 0

        for i in nums:
            prefix += i
            largest = max(largest, prefix)

            if prefix < 0:
                prefix = 0

        return largest