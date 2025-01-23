'''
Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.
Input: s1 = "1101", s2 = "111"
Output: 10100
Explanation:
 1101
+ 111
10100
'''
class Solution:
    def trimLeadingZeros(self,s):
        firstOne=s.find('1')
        return s[firstOne:]if firstOne!=-1 else "0"
def addBinary(self, s1, s2):
		# code here
		
        s1=self.trimLeadingZeros(s1)
        s2=self.trimLeadingZeros(s2)
        
        n=len(s1)
        m=len(s2)
        
        if n<m:
            s1,s2=s2,s1#s2 becomes smaller and s1 becomes larger string
            n,m=m,n
        j=m-1#j reach at end of string s2
        carry=0
        result=[]
        
        for i in range(n-1,-1,-1):#traverse from end of string of len of s1
            bit1=int(s1[i])
            bitsum=bit1+carry
            
            if j>=0:
                bit2=int(s2[j])
                bitsum+=bit2
                j-=1
            bit=bitsum%2
            carry=bitsum//2
            result.append(str(bit))
        if carry>0: # end carry
            result.append("1")
        return ''.join(result[::-1]) #reverse the result string cz storing done on bitsum from left to right