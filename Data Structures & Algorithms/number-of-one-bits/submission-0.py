class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for _ in range(32):
            bit = n & 1
            if bit:
                count += 1
            n = n >> 1
        return count        