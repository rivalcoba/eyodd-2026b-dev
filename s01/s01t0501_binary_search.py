
def binary_search(arr, target):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
      return mid
    elif target < arr[mid]:
      right = mid - 1
    else:
      left = mid + 1

  return -1

numbers = [3, 7, 12, 18, 21, 27, 35, 42, 56, 60]
print(binary_search(numbers, 35))