#***********Q1**********#
# Time Complexity : O(n)
class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True
        return False
    
    #***********Q2**********#
    class Solution(object):
    def isStrobogrammatic(self, num):
      
        maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
        i,j = 0, len(num) - 1
        while i <= j:
            if (num[i], num[j]) not in maps:
                return False
            i += 1
            j -= 1
        return True
    
     #***********Q3**********#
    class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        def str2int(num):
            numDict = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5,
                  '6' : 6, '7' : 7, '8' : 8, '9' : 9}
            output = 0
            for d in num:
                output = output * 10 + numDict[d]
            return output
        
        return str(str2int(num1) + str2int(num2)) 
    
     #***********Q4**********#
     def reverseWords_manual(s):  # O(n) both
    res = ''
    l, r = 0, 0
    while r < len(s):
        if s[r] != ' ':
            r += 1
        elif s[r] == ' ':
            res += s[l:r + 1][::-1]
            r += 1
            l = r
    res += ' '
    res += s[l:r + 2][::-1]
    return res[1:]


     #***********Q5**********#
     class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        temp = []
        first = 0
        last = k-1                 
        while (first <= len(s)-1):     
            if last > len(s)-1:
                last = len(s) - 1
            while(last >= first): 
                temp.append(s[last])  
                last = last - 1
            first = first + k                 
            last = first + (k-1)
            while(last >= first):
                if first > len(s)-1:
                    break
                temp.append(s[first])  
                first = first + 1                
            last = first + (k-1)       
        return ''.join(temp)
    
    
          #***********Q6**********#
          """
KMP algorithm
time: O(N)
space: O(N)
"""

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if len(A) == 0: return True
        
        # capture length of strings
        # then make both strings 1 indexed
        N = len(A)
        A = " " + A + A
        B = " " + B
        
        # calculate pi table, it captures the length of the
		# longest prefix that is also the suffix
        pi = [0] * (N+1)
        left, pi[0] = -1, -1
        for right in range(1, N+1):
            while left >= 0 and B[left + 1] != B[right]:
                left = pi[left]
            left += 1
            pi[right] = left
        
        # do matching
        j = 0
        for i in range(1, (2*N)+1):
            while j >= 0 and B[j+1] != A[i]:
                j = pi[j]
            j += 1
            if j == N: return True
        
        return False
    

        
        #***********Q7**********#
        class Solution:
	def backspaceCompare(self, S, T):
		i = len(S) - 1			# Traverse from the end of the strings
		j = len(T) - 1

		skipS = 0              # The number of backspaces required till we arrive at a valid character
		skipT = 0

		while i >= 0 or j >= 0:
			while i >= 0:					# Ensure that we are comparing a valid character in S
				if S[i] == "#" :
					skipS += 1				# If not a valid character, keep times we must backspace.
					i = i - 1

				elif skipS > 0:
					skipS -= 1				# Backspace the number of times calculated in the previous step
					i = i - 1

				else:
					break

			while j >= 0:					# Ensure that we are comparing a valid character in T
					if T[j] == "#":
						skipT += 1			# If not a valid character, keep times we must backspace.
						j = j - 1

					elif skipT > 0:
						skipT -= 1			# Backspace the number of times calculated in the previous step
						j = j - 1

					else:
						break

			print("Comparing", S[i], T[j])		# Print out the characters for better understanding.

			if i>= 0 and j >= 0 and S[i] != T[j]:    # Compare both valid characters. If not the same, return False.
				return False

			if (i>=0) != (j>=0):		# Also ensure that both the character indices are valid. If it is not valid,
				return False			#  it means that we are comparing a "#" with a valid character.

			i = i - 1
			j = j - 1

		return True					# This means both the strings are equivalent.



        #**********Q8*******#
        class Solution:
    def checkStraightLine(self, coordinates):
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x - x0) * (y1 - y0) != (y - y0) * (x1 - x0):
                return False

        return True

    

            
