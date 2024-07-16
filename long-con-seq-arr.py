#longest sub-sequence means that elements in the sub-sequence are consecutive integers, the consecutive numbers can be in any order.
def long_con_seq(list):
    new_set=set(list)
    longest=0
    for i in list:
        if (i-1) not in new_set:
            length=0
            while (i+length) in new_set:
                length+=1
                longest=max(length,longest)
    return longest
list=[2,4,1,9,7,8,6,10,3]
print("The longest consecutive sequence in a array is",end=" ")
print(long_con_seq(list))