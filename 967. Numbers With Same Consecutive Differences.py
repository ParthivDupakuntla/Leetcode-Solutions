class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]
        res = []
        def dfs(n,num):
            if n == 0: #base case
                return res.append(num)
            lastdigit = num%10
            nextdigits = set([lastdigit+k, lastdigit-k]) #use set to avoid duplicates when k = 0
            for i in nextdigits:
                if i in range(10):
                    newnum = num*10 + i
                    dfs(n-1, newnum)
        
        for num in range(1,10):
            dfs(n-1,num)
        return res
