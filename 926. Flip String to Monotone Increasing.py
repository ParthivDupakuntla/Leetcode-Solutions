# calculating number of ones to switch from right to left
# number of zeros to switch from left to right
# take minimum at each index, that is the answer
#Prefix Sum
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeros = s.count("0")
        ones = 0
        answer = zeros
        for d in s:
            if d == "0":
                zeros -=1
            elif d == "1":
                ones +=1
            answer = min(answer, zeros+ones)
        return answer
