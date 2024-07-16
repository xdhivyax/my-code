#Move all the negative elements to one side of the array 
arr=[2,1,3,5,-1,-8,-3,0,9,-5,8,0,4,-6,-2,-7]
new_arr=[]
for i in arr:
    if i<0:
        new_arr.append(i)
for i in arr:
    if i==0:
        new_arr.append(i)
for i in arr:
    if i>0:
        new_arr.append(i)
print(new_arr)

#another method
  
  #arr.sort()
arr.sort(reverse=True)
print(arr)