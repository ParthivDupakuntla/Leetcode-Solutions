# same as longest substring with 2 distinct characters
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right = 0,0
        mapp = defaultdict(int)
        ans = 0
        while right < len(fruits):
            mapp[fruits[right]] = right # update the fruit's value to its right most index
            if len(mapp) > 2:
                smallestIdx = min(mapp.values())
                del mapp[fruits[smallestIdx]]
                left = smallestIdx + 1
            ans = max(ans, right-left+1)
            right+=1
        return ans
