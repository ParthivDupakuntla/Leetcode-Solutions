class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        '''
        initialize dp array
        definition: dp[i] is the maximum sum that can be obtained at ith index using atmost k steps
        '''
        score = [0 for i in range(len(nums))]
        #first score would be the value at first index
        score[0] = nums[0]
        '''declare a monotonically decreasing queue always keep the maximum value in the range i-k to i-1 in the queue because that is the maximum in taking atmost k steps back from i up until i
        '''
        dq = deque()
        dq.append(0)
        
        for i in range(1, len(nums)):
            while dq and dq[0] < i-k:
                dq.popleft() #Pop all the indexes smaller than i-k out of dq from left.
            score[i] = score[dq[0]] + nums[i] #Update score[i] to score[dq.peekFirst()] + nums[i].
            while dq and score[i] >= score[dq[-1]]:
                dq.pop()
            dq.append(i)
        return score[-1]
