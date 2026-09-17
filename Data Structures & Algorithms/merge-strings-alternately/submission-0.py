class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(max(len(word1), len(word2))):
            if i >= len(word1):
                res += word2[i:]
                break
            elif i >= len(word2):
                res += word1[i:]
                break
            else:
                res += word1[i]
                res += word2[i]
            
        return res
            

        