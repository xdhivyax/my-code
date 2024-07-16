arr=[]
num=int(input("Enter the number:"))
for i in range(num):
    element=int(input())
    arr.append(element)
min=arr[0]
for i in range(num):
    if arr[i]<min:
        min=arr[i]
print("Minimum element in the array is",min)