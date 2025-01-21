'''Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular.

Examples:

Input: arr[] = [8, -8, 9, -9, 10, -11, 12]
Output: 22
Explanation: Starting from the last element of the array, i.e, 12, and moving in a circular fashion, we have max subarray as 12, 8, -8, 9, -9, 10, which gives maximum sum as 22.
'''
def circularSubarraySum(arr):
    ##Your code here
    totalSum=0
    currMax=0
    maxSum=arr[0]
    currMin=0
    minSum=arr[0]
    for i in range(len(arr)):
        currMax=max(currMax+arr[i],arr[i])

        maxSum=max(maxSum,currMax)

        currMin=min(currMin+arr[i],arr[i])

        minSum=min(minSum,currMin)

        totalSum+=arr[i]
    normalSum=maxSum
    circularSum=totalSum-minSum
    if minSum==totalSum:#case where whole array is negative
        return normalSum
    return max(normalSum,circularSum)
if __name__=="__main__":
  arr=[8, -8, 9, -9, 10, -11, 12]
  print(circularSubarraySum(arr))
