def rotation_of_array(array,l,k):
    temp=[]
    i=0
    while i<k:
        temp.append(array[i]) 
        i=i+1
    i=0
    while k<l:
        array[i]=array[k]
        i=i+1
        k=k+1
    array=array[:i]+temp
    return array
array=[1,2,3,4,5,6]
l=len(array)
k=int(input("Enter the position:"))
print(rotation_of_array(array,l,k))

#Another method

arr=[1,2,3,4,5]
rot_count=int(input())
res=[]
if(rot_count==0 or rot_count%len(arr)==0):
    res=arr
else:
    left_part=rot_count%len(arr)
res=arr[left_part:]+arr[:left_part]
print(res)