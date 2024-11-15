class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
#         own solution, idea is to traverse from end to start when the requirement is to modify in place
        count = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums.pop(i)
            else:
                count+=1
        return count
        
