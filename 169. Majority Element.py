class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore crux is that it is impossible to discard more majority elements than minority elements
        count = 0
        candidate = None
        for i in nums:
            if count == 0:
                #change the candidate
                candidate = i
            # keep counting for the current majority candidate. replace current candidate by the element in the next index if count reaches 0
            count +=1 if i == candidate else -1
        
        
        # for i in nums:
        #     if count == 0:
        #         candidate = i
        #     if i == candidate:
        #         count+=1
        #     else: count-=1
        return candidate

# this is what i came up with using hmap takes O(N) memory and time, Boyer Moore takes linear time but constant memory        
#         p = len(nums)/2
#         hmap = collections.defaultdict(int)
#         for i in nums:
#             hmap[i]+=1
#         for i in hmap:
#             if hmap[i] > p:
#                 return i
#         # return max(hmap.keys(), key =hmap.get)
            
            
        
