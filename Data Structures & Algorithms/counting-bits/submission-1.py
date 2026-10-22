class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]*(n+1)
        offset = 1
        for i in range(1, n+1):
            if(i == offset*2):
                offset *= 2
            arr[i] = 1 + arr[i - offset]
        return arr

    