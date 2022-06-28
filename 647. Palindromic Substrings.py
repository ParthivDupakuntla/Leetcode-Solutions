class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            res += self.pali(s, i,i)
            # l =  r = i
            # while l >= 0 and r < len(s) and s[l] == s[r]:
            #     res +=1
            #     l-=1
            #     r+=1
 
                
        for i in range(len(s)):
            res += self.pali(s, i, i+1)
            # while k >= 0 and m < len(s) and s[k] == s[m]:
            #     res +=1
            #     k -=1
            #     m +=1
                

        return res
    
    def pali(self, s, i,j):
        res = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            res +=1
            i-=1
            j+=1
        return res
                
        
