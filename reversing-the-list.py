def reverse_list(L,start,end):
    while(start<end):
        L[start],L[end]=L[end],L[start]
        start+=1
        end-=1
    print(L)
L=[10,20,30,40,50]
start=0
end=len(L)-1
reverse_list(L,start,end)

#Using slicing

List=[1,2,3,4,5]
print(List[::-1])