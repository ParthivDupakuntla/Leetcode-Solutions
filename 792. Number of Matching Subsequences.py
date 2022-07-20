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
    
    #more readable version, use a dict to store buckets of words, iterate over and append the remaining words
 class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        di = defaultdict(list)
        for word in words:
            di[word[0]].append(word)
        print(di)
        res = 0
        
        for char in s:
            words_expecting_char = di[char]
            di[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    res+=1
                else:
                    di[word[1]].append(word[1:])
            
        return res
