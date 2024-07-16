def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=merge_sort(arr[:mid])
    right_half=merge_sort(arr[mid:])
    return merge(left_half,right_half)
def merge(left,right):
    i=j=0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [1,5,7,3,9,2,6]
print("the merged array is",merge_sort(arr))

