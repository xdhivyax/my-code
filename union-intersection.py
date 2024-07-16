def union(list1,list2):
    new_list=[]
    for i in list1:
        if i not in new_list:
            new_list.append(i)
    for j in list2:
        if j not in new_list:
            new_list.append(j)
    print("The union is",new_list)
def intersection(list1,list2):
    new_list=[]
    for i in list1:
        if (i not in new_list) and (i in list2):
            new_list.append(i)
    print("The intersection is",new_list)
list1=[1,2,3,4,5]
list2=[4,3,2,6,7]
union(list1,list2)
intersection(list1,list2)
