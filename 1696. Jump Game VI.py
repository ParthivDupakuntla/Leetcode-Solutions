class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        score = [0 for i in range(len(nums))]
        score[0] = nums[0]
        dq = deque()
        dq.append(0)
        for i in range(1, len(nums)):
            while dq and dq[0] < i-k:
                dq.popleft()
            score[i] = score[dq[0]] + nums[i]
            while dq and score[i] >= score[dq[-1]]:
                dq.pop()
            dq.append(i)
        return score[-1]
