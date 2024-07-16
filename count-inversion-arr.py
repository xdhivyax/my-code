#Inversion count of a number means how close the array is to be sorted
#Two elements a[i] and a[j] form an inversion only if a[i] > a[j] and i < j.
array=[4,5,2,11,8,1]
n=len(array)
count=0
for i in range(n):
    for j in range(i+1,n):
        if array[i]>array[j]:
            count+=1
print("The inversion count of the array is",count)