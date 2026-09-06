class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            build = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if left == right:
                    build = s[left]
                else:
                    build = s[left] + build + s[right]

                left -= 1
                right += 1

            return build

        long = ""
        for i in range(len(s)):
            l = expand(i, i)
            r = expand(i, i + 1)

            if len(l) > len(long):
                long = l
            if len(r) > len(long):
                long = r


        return long

