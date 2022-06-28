#Optimised using maxf, where we fetch the max frequency and store it instead of fetching the max value of the hashmap in every iteration
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l, res = 0, 0 
        maxf = 0
        for r in range(len(s)):
            count[s[r]] +=1
            maxf = max(maxf, count[s[r]])
            if ((r - l + 1) - maxf) > k:
                count[s[l]] -=1
                l +=1
            res = max(res, r-l+1)
        return res
        
#Standard O(26n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l, res = 0, 0 
        for r in range(len(s)):
            count[s[r]] +=1
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -=1
                l +=1
            res = max(res, r-l+1)
        return res
    
