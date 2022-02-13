#Using Stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        answer = []
        for a in asteroids:
            while answer and a < 0 and answer[-1] > 0:
                if -a == answer[-1]:
                    answer.pop()
                    break
                elif answer[-1] < -a:
                    answer.pop()
                    continue
                else:
                    break
                
            else:
                answer.append(a)
        return answer
                
