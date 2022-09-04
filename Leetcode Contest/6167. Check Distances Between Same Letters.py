#Weekly Contest 309
'''
You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly twice. You are also given a 0-indexed integer array distance of length 26.

Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).

In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i]. If the ith letter does not appear in s, then distance[i] can be ignored.

Return true if s is a well-spaced string, otherwise return false.

Ex 1:
Input: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: true
Explanation:
- 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
- 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
- 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
Return true because s is a well-spaced string.

Ex 2:
Input: s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: false
Explanation:
- 'a' appears at indices 0 and 1 so there are zero letters between them.
Because distance[0] = 1, s is not a well-spaced string.
'''

#My Code
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        res = [0]*26
        i = 0 
        j = 1
        charset = set()
        while i < len(s):
            if s[i] not in charset:
                while s[j]!= s[i]:
                    j+=1
                res[ord(s[i])-ord('a')] = j-i-1
            charset.add(s[i])
            i+=1
            j = i+1
        print(charset)        
        k=0
        print(res)
        while k < len(distance):
            # print(chr(res[k]+ord('a')))
            char = chr(k+ord('a'))
            if char in charset:
                print(char)
                if distance[k]!=res[k]:
                    return False
            k+=1
        return True
        
