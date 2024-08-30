def heapify(array, a, b):
    largest = b
    l = 2*b + 1
    root = 2*b + 2
    if l<a and array[b]<array[l]:
        largest = l
    if root<a and array[largest]<array[root]:
        largest = root
    if largest != b:
        array[b], array[largest] = array[largest], array[b]
        heapify(array, a, largest)

def heap_sort(array):
    a = len(array)
    for b in range(a//2-1,-1,-1):
        heapify(array, a, b)
    for b in range(a-1, 0, -1):
        array[b], array[0] = array[0], array[b]
        heapify(array, b, 0)
array = [7,5,4,8,0,9,66,57]
print(f"original array: {array}")
heap_sort(array)
print(f"Array after sorting:{array}")