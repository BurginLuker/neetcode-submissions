class Solution:
    def climbStairs(self, n: int) -> int:
        options = [0, 1, 2]

        for i in range(3, n + 1):
            u = options[i - 1] + options[i - 2]
            options.append(u)

        return options[n]