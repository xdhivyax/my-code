# to find the subarray such that the sum of it is maximum amongst all the possible subarray.
array=[-1, 8, 1, -7, -1, 5, 1, -3]
l=len(array)
sub_array=[]
max_sum=-1
for i in range(l):
    for j in range(i,l):
        a=sum(array[i:j+1])
        if a>max_sum:
            max_sum=a
            sub_array=array[i:j+1]

print("The sub array is",sub_array)
print("The sum of the sub array is",max_sum)
        