def next_permutation(arr):
    n = len(arr)
    pivot = -1

    # Step 1: Find the pivot
    for i in range(n - 2, -1, -1):  # Start from the second last element
        if arr[i] < arr[i + 1]:
            pivot = i
            break

    # Step 2: If no pivot exists, reverse the array and return
    if pivot == -1:
        arr.reverse()
        return

    # Step 3: Find the smallest element greater than pivot from the right
    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]  # Swap
            break

    # Step 4: Reverse the part of the array from pivot + 1 to the end
    arr[pivot + 1:] = reversed(arr[pivot + 1:])

