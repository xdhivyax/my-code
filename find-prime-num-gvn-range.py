start,end=1,8
prime=[]
for i in range(start,end+1):
    flag=0
    if i<2:
        continue
    if i==2:
        prime.append(i)
        continue
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        prime.append(i)
print(prime)
    