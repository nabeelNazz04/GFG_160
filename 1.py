'''
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
'''
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n=len(arr)
        largest=-1
        secondlargest=-1
        for num in arr:
            if num>largest:
                secondlargest=largest
                largest=num
            elif num>secondlargest and num!=largest:
                secondlargest=num
        if secondlargest!=-1:
            return secondlargest
        else:
            return -1
            
