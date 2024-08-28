def MergeSort(arr, start, end):
    if start >= end:
        return arr[start:end+1] 

    mid = start + (end - start) // 2
    left = MergeSort(arr, start, mid)
    right = MergeSort(arr, mid + 1, end)
    return merge(left, right)

def merge(left, right):
    ans = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    while i < len(left):
        ans.append(left[i])
        i += 1
    while j < len(right):
        ans.append(right[j])
        j += 1

    return ans

arr = [3, 2, 4, 5, 2, 1]
result = MergeSort(arr, 0, len(arr) - 1)
print(result)
