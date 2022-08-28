class Solution:
    def countVowelPermutation(self, n: int) -> int:
        #a,e,i,o,u -> 0,1,2,3,4
        acount = ecount = icount = ocount = ucount = 1
        mod = 10**9 + 7
        for i in range(1,n):
            acountnew = (ecount + icount + ucount) % mod
            ecountnew = (acount + icount) % mod
            icountnew = (ecount + ocount) % mod
            ocountnew = (icount) % mod
            ucountnew = (icount + ocount) % mod
            
            acount, ecount, icount, ocount, ucount = acountnew, ecountnew, icountnew, ocountnew, ucountnew
            
        return (acount + ecount + icount + ocount + ucount) % mod
