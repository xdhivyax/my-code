string=input("Enter the string: ")
for i in string:
    count=0
    for j in string:
        if i==j:
            count+=1
            if count>1:
                break
    if count==1:
        print(i,end=" ")
print()
        