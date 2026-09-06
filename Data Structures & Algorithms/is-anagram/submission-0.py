class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        HM1 = {}
        HM2 = {}
        for c in s:
            if c not in HM1:
                HM1[c] = 1
            else:
                HM1[c] += 1
        for c in t:
            if c not in HM2:
                HM2[c] = 1
            else:
                HM2[c] += 1
        for key in HM1:
            if (key not in HM2) or (HM1[key] != HM2[key]):
                return False
        return True