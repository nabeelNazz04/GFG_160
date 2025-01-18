# Maximum product of subarrays
class Solution:
    """
    A class to implement the algorithm for finding the maximum product of a contiguous subarray.
    """

    # Function to find the maximum product subarray
    def maxProduct(self, arr):
        # Initialize the current minimum, current maximum, and overall maximum product
        currMin = arr[0]
        currMax = arr[0]
        maxProd = arr[0]

        # Iterate through the array starting from the second element
        for i in range(1, len(arr)):
            # Calculate the new current maximum (store in a temporary variable)
            temp = max(arr[i], arr[i] * currMin, arr[i] * currMax)

            # Update the current minimum
            currMin = min(arr[i], arr[i] * currMin, arr[i] * currMax)

            # Update the current maximum using the temporary value
            currMax = temp

            # Update the overall maximum product
            maxProd = max(maxProd, currMax)

        return maxProd


if __name__ == "__main__":
    # Example input array
    arr = [-2, 6, -3, -10, 0, 2]

    # Creating an object of the Solution class
    s = Solution()

    # Printing the result of the maximum product of subarrays
    print(s.maxProduct(arr))
'''
1.Variable Initialization:
-----------------------------
currMin and currMax track the minimum and maximum products at each step since a negative number multiplied by a minimum value can become the maximum.
maxProd keeps track of the overall maximum product.

2.Temporary Variable temp:
-----------------------------
This is essential to store the updated value of currMax before using it to update currMin, avoiding logical errors.

3.Iterative Update:
-----------------------
For each element in the array, the maximum and minimum products are recalculated using all three possibilities:
The current element alone (arr[i]).
The current element multiplied by the previous currMin.
The current element multiplied by the previous currMax.

4.Final Update:
-----------------------
maxProd is updated with the larger of its current value and the newly computed currMax.
'''