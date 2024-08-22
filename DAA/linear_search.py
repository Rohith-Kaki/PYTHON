def linearSearch(arr, start, end, target):
    if(arr[start] == target):
        return start
    if start == end:
        return -1
    else:
        return linearSearch(arr,start+1,end,target)



arr = [1,2,3,4,5,6,7,0,8,9]
ans = linearSearch(arr,0,len(arr)-1,2)
print(ans)