'''
You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.
'''
#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
            count=0
            for i in range(len(arr)):
              if arr[i]!=0:
                arr[count],arr[i]=arr[i],arr[count]#swap
                count+=1
        #time complexity n and space complexity 
        # code wih space complexity 2n
        '''
      count=0
      n=len(arr)
      temp=[0]*n
      for i in range(n)
      if arr[i]!=0:
        temp[count]=arr[i]
        count+=1
      while(count!=n):
        temp[count]=0
        count+=1
       '''

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends