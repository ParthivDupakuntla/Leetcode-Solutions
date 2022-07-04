class Solution:
    def candy(self, ratings: List[int]) -> int:
        l2r = [1 for i in range(len(ratings))]
        r2l = [1 for i in range(len(ratings))]
        res = []
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                l2r[i] = l2r[i-1] + 1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                r2l[i] = r2l[i+1] + 1
        for i in range(len(ratings)):
            res.append(max(l2r[i], r2l[i]))
        return sum(res)
            
                           
        
