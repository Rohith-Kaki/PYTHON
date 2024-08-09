list = [1,2,3,5,6,4]
len = len(list)
for i in range(0,len):
    for j in range(0,len - i-1):
        if(list[j] < list [j-1]):
            temp = list[j];
            list[j] = list[j-1];
            list[j-1] = temp;
            
print(list)