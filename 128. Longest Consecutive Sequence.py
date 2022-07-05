class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        long = 0
        for i in numset:
            if i-1 not in numset: #check if the number is the start of a sequence
                length = 0 #init length of current sequence
                while i+length in numset: #check for consecutive number
                    length+=1
                long = max(long, length )
        return long
            
