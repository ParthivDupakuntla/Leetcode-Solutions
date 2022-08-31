#Sliding Window pattern
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        
        for right in range(len(nums)): #using the pointer as the variable in the for loop, good technique to increment pointer on every iteration
            if nums[right] == 0:
                k-=1 #decrement k if we see a zero
            
            if k < 0:
                if nums[left] == 0:
                    k+=1 #if a zero is removed from the window, k needs to be incremented
                left +=1 #regardless of seeing a 0 or 1, we move the left side by 1. Window still moves if we keep seeing 1s. So as long as k is -ve, window keeps moving so that we can eventually adjust k if we see a zero.
        
        return right - left + 1
