def binary_search(arr, start, end, x):
    if end >= start:
        mid = start + (end - start) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, start, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, end, x)
    else:
        return -1


arr = list(map(int, input("Enter the array elements separated by space: ").split()))

x = int(input("Enter the element to be searched: "))

result = binary_search(arr, 0, len(arr) - 1, x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in the array")
