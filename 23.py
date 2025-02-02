class Solution:
    # Function to count inversions in the array
    def inversionCount(self, arr):
        """
        Count the number of inversions in the array using Merge Sort.

        Parameters:
        arr (List[int]): The input array.

        Returns:
        int: The number of inversions.
        """
        # Helper function to perform merge sort and count inversions
        def mergeSortAndCount(arr):
            # Base case: If the array has 1 or 0 elements, it is already sorted
            if len(arr) <= 1:
                return arr, 0
            
            # Divide the array into two halves
            mid = len(arr) // 2
            left, invLeft = mergeSortAndCount(arr[:mid])  # Sort the left half
            right, invRight = mergeSortAndCount(arr[mid:])  # Sort the right half
            merged, invMerge = mergeAndCount(left, right)  # Merge the two halves and count inversions
            
            # Total inversions = inversions in left + inversions in right + inversions during merge
            totalInversions = invLeft + invRight + invMerge
            return merged, totalInversions

        # Helper function to merge two sorted arrays and count inversions
        def mergeAndCount(left, right):
            result = []
            inversions = 0
            i = j = 0
            
            # Merge the two arrays
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
                    # If left[i] > right[j], it forms inversions with all remaining elements in left
                    inversions += len(left) - i
            
            # Append any remaining elements from left or right
            result.extend(left[i:])
            result.extend(right[j:])
            
            return result, inversions

        # Call the helper function and return the total number of inversions
        _, totalInversions = mergeSortAndCount(arr)
        return totalInversions


# Main function to test the Solution class
if __name__ == "__main__":
    # Input array
    arr = [8, 4, 2, 1]
    
    # Create an instance of the Solution class
    s = Solution()
    
    # Calculate and print the number of inversions
    print("Number of inversions:", s.inversionCount(arr))