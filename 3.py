'''
ou are given an array of integers arr[]. Your task is to reverse the given array.
'''
class Solution:
    def reverseArray(self, arr):
        # code here
      n=len(arr)
      for i in range(n//2):
        arr[i],arr[n-1-i]=arr[n-1-i],arr[i]#swaping first and last
    
        #time complexity n and space complexity 1