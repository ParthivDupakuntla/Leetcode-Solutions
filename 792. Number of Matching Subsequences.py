class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        heads = [[]for i in range(26)]
        for word in words:
            it = iter(word)
            heads[ord(next(it)) - ord('a')].append(it)
        
        for l in s:
            l_index = ord(l) - ord('a')
            old_bucket = heads[l_index]
            heads[l_index] = []
            
            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    res +=1
        return res
