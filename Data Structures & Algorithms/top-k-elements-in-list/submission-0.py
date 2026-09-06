from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = Counter(nums)
        HM = defaultdict(list)
        for key, value in count.items():
            HM[value].append(key)
        for i in range(len(nums), 0, -1):
            if len(result) != k and i in HM:
                for n in HM[i]:
                    result.append(n)
        return result



        