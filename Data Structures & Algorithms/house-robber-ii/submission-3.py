class Solution:
    def rob(self, nums: List[int]) -> int:        
        def getBest(houses):
            if len(houses) == 0:
                return 0
            if len(houses) == 1:
                return houses[0]
            
            best = [0] * len(houses)
            best[0] = houses[0]
            best[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                best[i] = max(best[i - 1], best[i - 2] + houses[i])

            return best[-1]

        if(len(nums) == 1):
            return nums[0]

        b1 = getBest(nums[0:len(nums) - 1])
        b2 = getBest(nums[1:len(nums)])

        return max(b1, b2)