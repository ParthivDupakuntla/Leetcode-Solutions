class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            row = [0 for i in range(i+1)]
            row[0] = row[-1] = 1
            for j in range(1,len(row)-1):
                row[j] = ans[i-1][j-1] + ans[i-1][j]
            ans.append(row)
        return ans
