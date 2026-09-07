class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = nums[0]

        big = 1
        small = 1

        for i in nums:
            temp = big * i

            big = max(temp, small * i, i)
            small = min(temp, small * i, i)

            largest = max(largest, big)

        return largest