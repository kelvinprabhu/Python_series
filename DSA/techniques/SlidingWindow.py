# sliding window technique - An efficient way to solve problems involving subarrays or substrings
#  Time Complexity: O(n)
#  Space Complexity: O(1)
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1  # Not enough elements for the window size

    # Calculate the sum of the first window
    max_sum = sum(arr[:k])
    window_sum = max_sum

    # Slide the window from start to end of the array
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]  # Add next element and remove the first element of the previous window
        max_sum = max(max_sum, window_sum)  # Update max_sum if needed

    return max_sum