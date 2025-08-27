class Solution:
    def reverse(self, x: int) -> int:
        int_max = 2**31 - 1
        int_min = -2**31

        rev = 0
        while x != 0:
            pop = int(x % 10) if x > 0 else int(x % -10)
            x = (x - pop) // 10

            if rev > int_max // 10 or (rev == int_max // 10 and pop > 7):
                return 0
            if rev < int_min // 10 or (rev == int_min // 10 and pop < -8):
                return 0

            rev = rev * 10 + pop

        return rev
