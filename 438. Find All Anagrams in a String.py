class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = [] #initialise result list
        mapp = [0] * 26 #initialize an array of 26 size, each denoting the frequency of a letter in p
        for char in p:
            mapp[ord(char)-ord('a')] +=1 #create the array with frequencies
        i,j, length = 0,0, len(p) #2 pointers and have a length of the pattern
        while j < len(s):#to be in bounds, j is the right pointer 
            if mapp[ord(s[j]) - ord('a')] > 0:#if you have the frequency of s[j] already in the array, decrease the length, this is equal to checking the permutation
                length -=1
            mapp[ord(s[j]) - ord('a')] -=1 #after you decrease the length, you have to decrease the frequency
            j+=1 #end while loop, like till this step, we are checking to see an anagram.
            if length == 0:#if we found an anagram, add the starting index, which is i to the result list
                res.append(i)
            if j-i == len(p):#if the window size is equal to the length of the pattern
                if mapp[ord(s[i]) - ord('a')] >= 0:#if the frequency of the character at the left pointer is greater than or equal to zero
                    length+=1 #increase the length
                mapp[ord(s[i])-ord('a')]+=1 #increase the frequency count of the left pointer character in the array
                i+=1#slide the window by increasing left pointer
        return res #return result list
