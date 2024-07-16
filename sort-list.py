List=[]
num=int(input("Enter the number of element in the List:"))
for i in range(num):
    element=int(input())
    List.append(element)
print(List)
List.sort()
print(List)