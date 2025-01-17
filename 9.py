'''
Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.

Examples :

Input: k = 2, arr[] = {1, 5, 8, 10}
Output: 5
Explanation: The array can be modified as {1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}.The difference between the largest and the smallest is 8-3 = 5.
'''
class Solution:
    def getMinDiff(self, arr, k):
        # Sort the array to allow logical indexing
        arr.sort()
        n = len(arr)
        
        # Initial difference between max and min heights
        result = arr[n-1] - arr[0]
        
        # Iterate through the array to calculate potential min and max heights
        for i in range(1, n):
            # If reducing arr[i] by k results in a negative height, skip this iteration
            if arr[i] - k < 0:
                continue
            
            # Calculate the new minimum height:
            # 1. Either reduce the current element arr[i] by k
            # 2. Or increase the smallest element arr[0] by k
            # We choose the smaller of these two possibilities.
            minH = min(arr[i] - k, arr[0] + k)
            
            # Calculate the new maximum height:
            # 1. Either increase the previous element arr[i-1] by k
            # 2. Or reduce the largest element arr[n-1] by k
            # We choose the larger of these two possibilities.
            maxH = max(arr[i-1] + k, arr[n-1] - k)
            
            # Update the result with the smallest range
            result = min(result, maxH - minH)
        
        return result
if __name__=="__main__":
  k = 2
  arr = [1, 5, 8, 10]
  s=Solution()
  print(s.getMinDiff(arr,k))