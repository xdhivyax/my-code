array=[12,3,12,55,77,8,6,55,6]
n=len(array)
for i in range(n):
    count=0
    for j in range(n):
        if array[i]==array[j]:
            count+=1
            if count >1:
                break
    if count ==1:
        print(array[i],end=" ")