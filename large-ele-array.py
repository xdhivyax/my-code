num=int(input("Enter the number:"))
arr=[]
for i in range(num):
    ele=int(input())
    arr.append(ele)
max=arr[0]
for i in range(num):
    if arr[i]>max:
        max=arr[i]
print("Maximum element in the array is",max)