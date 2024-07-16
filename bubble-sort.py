def bubble_sort(arr):
    length=len(arr)
    for i in range(length-1):
        for j in range(0,length-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[4,9,2,5,10,1,6]
print(bubble_sort(arr))