class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        countmap = [0]*26
        for i in range(len(s)):
            countmap[ord(s[i])-ord('a')]+=1
            countmap[ord(t[i])-ord('a')]-=1

        for x in countmap:
            if x!=0:
                return False
        return True