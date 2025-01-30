### Sort 0s, 1s and 2s
'''
Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.

You need to solve this problem without utilizing the built-in sort function.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.
'''
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        c0=0
        c1=0
        c2=0
        idx=0
        for num in arr:
            if arr[num]==0:
                c0+=1
            elif arr[num]==1:
                c1+=1
            elif arr[num]==2:
                c2+=1
        for i in range(c0):
            arr[idx]=0
            idx+=1
        for i in range(c1):
            arr[idx]=1
            idx+=1
        for i in range(c2):
            arr[idx]=2
            idx+=1