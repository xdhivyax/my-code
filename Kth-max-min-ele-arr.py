#to find kth max and min element of an array # user will enter k value as 2 to find the 2nd largest ele and 2nd smallest ele in the array
arr=[4,6,2,1,6,0,5,8,9]
k=int(input("Enter the k th element to find min and max:"))
def max(arr,k):
    arr.sort(reverse=True)
    print(arr)
    print(arr[k-1])
def min(arr,k):
    arr.sort()
    print(arr)
    print(arr[k-1])
max(arr,k)
min(arr,k)