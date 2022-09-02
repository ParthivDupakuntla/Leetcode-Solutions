class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        patternMap = [0]*26
        for c in s1:
            patternMap[ord(c)-ord('a')] +=1
        i,j,patternlen = 0,0, len(s1)
        while j < len(s2):
            if patternMap[ord(s2[j])-ord('a')] > 0:
                patternlen -=1
            patternMap[ord(s2[j])-ord('a')] -=1
            j+=1
            if patternlen == 0:
                return True
            if j-i == len(s1):
                if patternMap[ord(s2[i])-ord('a')] >=0:
                    patternlen +=1
                patternMap[ord(s2[i])-ord('a')]+=1
                i+=1
        return False
        
