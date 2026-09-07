class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def decode(i):
            if i in cache:
                return cache[i]

            if i >= len(s):
                return 1

            if s[i] == '0':
                return 0

            ways = decode(i + 1)

            if i + 1 <= len(s) - 1:
                if int(s[i] + s[i + 1]) <= 26:
                    ways += decode(i + 2)

            cache[i] = ways
            return ways

        
        return decode(0)

