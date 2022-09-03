class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = defaultdict(int)
        window = defaultdict(int)
        if s == "":
            return ""
        res = ""
        reslen = float("inf")
        #create frequency hashmap        
        for char in t:
            tcount[char]+=1
        l = 0
        have = 0
        need = len(tcount) #have is the number of chars we have and need is the number of chars we want
        #loop
        for r in range(len(s)):
            window[s[r]] +=1
            if s[r] in tcount and tcount[s[r]] == window[s[r]]:
                have +=1
            while have == need:
                if (r-l+1) < reslen:
                    reslen = r-l+1
                    res = s[l:r+1]
                window[s[l]] -=1 #pop left element
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    have -=1
                l+=1
        return res
                    
                
