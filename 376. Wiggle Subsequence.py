class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up  = collections.defaultdict(int)
        down = collections.defaultdict(int)
        
        up[0] = 1
        down[0] = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0:
                up[i] = max(up[i-1], down[i-1] + 1)
                down[i] = down[i-1]
            elif nums[i] - nums[i-1] < 0:
                down[i] = max(down[i-1], up[i-1] + 1)
                up[i] = up[i-1]
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
        return  max(up[len(nums)-1], down[len(nums)-1])
    
                
            
                
