'''
Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to merge all of the overlapping Intervals.

Examples:

Input: arr[][] = [[1,3],[2,4],[6,8],[9,10]]
Output: [[1,4], [6,8], [9,10]]
Explanation: In the given intervals we have only two overlapping intervals here, [1,3] and [2,4] which on merging will become [1,4]. Therefore we will return [[1,4], [6,8], [9,10]].

'''

class Solution:
    def mergeOverlap(self, arr):
        # Step 1: Sort the intervals based on their start times
        arr.sort()
        
        # Step 2: Initialize the result list with the first interval
        res = [arr[0]]
        
        # Step 3: Iterate through the sorted intervals starting from the second interval
        for i in range(1, len(arr)):
            # Get the last interval in the result list
            last = res[-1]
            # Get the current interval
            curr = arr[i]
            
            # Step 4: Check if the current interval overlaps with the last interval in the result
            if curr[0] <= last[1]:
                # If they overlap, merge them by updating the end time of the last interval
                last[1] = max(last[1], curr[1])
            else:
                # If they don't overlap, add the current interval to the result list
                res.append(curr)
        
        # Step 5: Return the list of merged intervals
        return res

# Example usage
if __name__ == "__main__":
    c = Solution()
    arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(c.mergeOverlap(arr))  # Output: [[1, 6], [8, 10], [15, 18]]