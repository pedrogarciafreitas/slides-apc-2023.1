def binary_search(array, target, first, last):
    if first <= last:
        mid = (first + last) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:  # primeira metade
            return binary_search(array, target, first, mid - 1)
        else:  # segunda metade
            return binary_search(array, target, mid + 1, last)
    return -1


def search(array, value):
    return binary_search(array, value, 0, len(array)-1)



print(search([ 2, 3, 4, 10, 40 ], 2))
print(search([ 2, 3, 4, 10, 40 ], 10))