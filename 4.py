'''
Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.
'''
#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n=len(arr)
        d%=n #handling outof bounds
        reverse(arr,0,d-1)#reverse until d th
        reverse(arr,d,n-1)#reverse from dth to end
        reverse(arr,0,n-1)#reverse the whole
def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
#time complexity n
#space complexity 1