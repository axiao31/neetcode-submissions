class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            s = 0
            temp = n
            while temp > 0:
                digit = temp % 10
                s += digit ** 2
                temp //= 10
            n = s

        return n == 1