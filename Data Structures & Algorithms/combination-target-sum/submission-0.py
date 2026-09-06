class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def findPath(total, path, i):
            if total == target:
                output.append(path)
                return
            if total > target:
                return

            for index, num in enumerate(nums[i:]):
                newList = list(path)
                newList.append(num)
                findPath(total + num, newList, index + i)

        findPath(0, [], 0)
        return output

