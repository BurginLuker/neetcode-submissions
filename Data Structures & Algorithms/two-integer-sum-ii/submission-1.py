class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while r > l:
            total = numbers[r] + numbers[l]

            if total == target:
                return [l + 1, r + 1]
            if total < target:
                l += 1
            else:
                r -= 1