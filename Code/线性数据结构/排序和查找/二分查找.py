# 必须要在有序表的情况下才能使用二分查找
def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    found = False
    while left <= right and not found:
        mid = (left + right) // 2
        if arr[mid] == target:
            found = True
        else:
            if target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return found

# 二分法也能用递归算法实现
def binarySearch2(arr, target):
    if len (arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if target == arr[mid]:
            return True
        else:
            if target < arr[mid]:
                return binarySearch2(arr[:mid], target)
            else:
                return binarySearch2(arr[mid + 1:], target)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch2(testlist, 3))
print(binarySearch(testlist, 13))
