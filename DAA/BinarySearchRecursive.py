def Binary_search(arr,target,start,end):
    if(start > end):
        return False
    mid = start + (end-start)//2
    if(arr[mid] == target):
        return True
    elif(arr[mid] > target):
        return Binary_search(arr,target,start,mid-1)
    else:
        return Binary_search(arr,target,mid+1,end)

    
arr = [1,2,3,4,5,6,7,9]
target = 9
ans = Binary_search(arr,target,0,len(arr)-1)
print(ans)