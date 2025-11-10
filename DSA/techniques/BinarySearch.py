# Binary search technique - An efficient way to find an element in a sorted array
# how it works: repeatedly divides the search interval in half
# Time Complexity: O(log n)
# Space Complexity: O(1)
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
left = 0
right = len(array) - 1
while left <= right:
    mid = left + (right - left) // 2  # Find the middle index
    print(f"Checking middle index {mid}, value {array[mid]}")
    if array[mid] == target:
        print(f"Element found at index {mid}")
        break
    elif array[mid] < target:
        left = mid + 1  # Search in the right half
    else:
        right = mid - 1  # Search in the left half
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  # Element found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    return -1  # Element not found