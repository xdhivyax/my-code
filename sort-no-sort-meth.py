list=[22,1,9,44,8]
n=len(list)
for i in range(n):
    for j in range(i+1,n):
        if list[i]>=list[j]:
            list[i],list[j]=list[j],list[i]
print("Sorted list is",list)